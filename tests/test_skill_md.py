"""The official olywork skill: served {BASE}-templated at GET /skill.md, and installed
to ~/.claude/skills/olywork/ by install.sh (so one curl gives a machine the CLI + the skill)."""

from __future__ import annotations

from pathlib import Path

from olywork import api as api_mod


async def test_skill_md_served_and_templated(clients):
    r = await clients.get("/skill.md")
    assert r.status_code == 200
    body = r.text
    assert body.startswith("---") and "name: olywork" in body  # loadable skill frontmatter
    assert "{BASE}" not in body                                        # fully templated
    # The own-tools call is taught by TOOL NAME, not by prefixing an arbitrary upstream URL. Both
    # resolve server-side, but "prefix any URL and we attach a credential" reads as an open
    # credential proxy — which is how OpenAI's policy scan took it. Only registered tools resolve;
    # say it that way.
    assert "/call/<tool-name>/<path>" in body
    assert "/call/https://" not in body
    assert "olywork register" not in body                                 # the retired command must not resurface


async def test_well_known_skills_index_advertises_the_skill(clients):
    """The agentskills.io convention: a host that serves this is itself a skill source, so olywork can
    be installed from olywork.com with no directory and no review queue in between."""
    r = await clients.get("/.well-known/skills/index.json")
    assert r.status_code == 200
    skills = r.json()["skills"]
    assert [s["name"] for s in skills] == ["olywork", "make-ugc"]
    entry = skills[0]
    assert entry["name"] == "olywork"
    assert entry["files"] == ["SKILL.md"]
    assert entry["description"], "the description is what registries index on"


async def test_well_known_skill_md_matches_the_canonical_one(clients):
    """The index promises this exact path. It must serve the SAME skill as /skill.md — a second copy
    that drifts is the whole failure mode the generated plugins exist to avoid."""
    r = await clients.get("/.well-known/skills/olywork/SKILL.md")
    assert r.status_code == 200
    assert "{BASE}" not in r.text                    # templated to the serving host, like /skill.md
    canonical = await clients.get("/skill.md")
    assert r.text == canonical.text


async def test_well_known_index_description_is_not_a_second_copy(clients):
    """It is read from the skill's own frontmatter at request time. If someone hard-codes it in
    api.py instead, this catches the moment the two disagree."""
    idx = await clients.get("/.well-known/skills/index.json")
    served = await clients.get("/skill.md")
    description = idx.json()["skills"][0]["description"]
    assert f"description: {description}" in served.text


async def test_make_ugc_skill_is_served_and_advertised(clients):
    """The /ugc workflow as a skill: one public URL an agent can be pointed at, the same file the
    well-known index promises, templated to the serving host like the core skill."""
    r = await clients.get("/skills/ugc/SKILL.md")
    assert r.status_code == 200 and r.text.startswith("---\nname: make-ugc")
    assert "{BASE}" not in r.text
    wk = await clients.get("/.well-known/skills/make-ugc/SKILL.md")
    assert wk.text == r.text
    idx = (await clients.get("/.well-known/skills/index.json")).json()["skills"][1]
    assert f"description: {idx['description']}" in r.text


def test_install_sh_installs_the_skill():
    sh = (Path(api_mod.__file__).parent / "web" / "install.sh").read_text()
    assert "$BASE/skill.md" in sh and ".claude/skills/olywork" in sh


def test_install_sh_supports_the_one_shot_authed_setup():
    """`… | sh -s -- --token <key>` (or OLYWORK_TOKEN=) → sign in + register MCP in one go; the key
    bakes in the team, so no org is passed. Without a token the flow is unchanged."""
    sh = (Path(api_mod.__file__).parent / "web" / "install.sh").read_text()
    assert "--token" in sh and "OLYWORK_TOKEN" in sh
    assert "olywork login --token" in sh
    assert "olywork mcp install" in sh
