const scene=new THREE.Scene(),camera=new THREE.PerspectiveCamera(56,1,.04,60);
let renderer;
try {
  renderer=new THREE.WebGLRenderer({antialias:true,alpha:true,powerPreference:'default'});
} catch (firstError) {
  try {
    renderer=new THREE.WebGLRenderer({antialias:false,alpha:true,powerPreference:'low-power'});
  } catch (error) {
    stage.style.height='auto';
    const message=document.createElement('p');
    message.setAttribute('role','alert');
    message.textContent='Your browser could not start 3D graphics (WebGL). Enable graphics acceleration in your browser settings, restart the browser, and reopen this page. You can also try another browser.';
    const retry=document.createElement('button');
    retry.className='btn';retry.type='button';retry.textContent='Reload walkthrough';
    retry.onclick=()=>location.reload();
    stage.replaceChildren(message,retry);
    detail.textContent='3D graphics unavailable on this browser.';
    root.querySelectorAll('button,select').forEach(control=>{if(control!==retry)control.disabled=true;});
    console.error('Unable to initialize WebGL',firstError,error);
    return;
  }
}
renderer.setPixelRatio(Math.min(devicePixelRatio,1.5));renderer.outputColorSpace=THREE.SRGBColorSpace;renderer.shadowMap.enabled=true;renderer.shadowMap.type=THREE.PCFSoftShadowMap;stage.appendChild(renderer.domElement);renderer.domElement.style.display='block';
renderer.domElement.addEventListener('webglcontextlost',event=>{
  event.preventDefault();
  detail.textContent='3D graphics paused. Waiting for the browser to restore graphics; reload if it stays blank.';
});
renderer.domElement.addEventListener('webglcontextrestored',()=>{detail.textContent='3D graphics restored.';});
