// Keep recovery outside the module graph: a failed dependency never executes gateway-3d.js.
import('./gateway-3d.js').catch(error => {
  const host = document.querySelector('.gateway-sculpture');
  if (host) host.dataset.modelState = 'fallback';
  window.olyworkOpening?.release();
  console.warn('3D gateway could not load; showing the olywork mark.', error);
});
