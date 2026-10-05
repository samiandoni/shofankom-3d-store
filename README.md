# Shofankom 3D Store

Interactive, measured 3D walkthrough of the Shofankom store.

**[Open the walkthrough](https://samiandoni.github.io/shofankom-3d-store/)**

## Explore

- On mobile, use the left thumb joystick to walk and drag the view with your other thumb to look around. Release the joystick to stop.
- On desktop, drag to look around and use arrow keys, WASD, or Forward / Back to move along the aisle.
- Scroll or use the zoom buttons to zoom.
- Select a photo section and inspect it up close.
- Switch to overview or plan to see the layout.
- Use Full screen to enlarge the walkthrough; select Exit full screen to return. Browsers without fullscreen support expand the viewer within the browser window.

The walkthrough supports desktop and mobile browsers with WebGL. Viewer libraries are pinned and hosted in this repository, so no external CDN is required.

## Project files

- `index.html`: browser walkthrough loading the store photos from separate files.
- `assets/shelves/`: shelf and rack reference photos, named by location or bay.
- `assets/fixtures/`: fridge, counter, and artwork reference photos.
- `source/store-measured.html`: original editable model source.
- `source/standalone-export.html`: standalone export used by the deployment preparation script.
- `source/renderer-compat.js`: graphics initialization with a lower-resource retry and visible errors.
- `vendor/`: pinned Three.js and viewer resources, including their license notices.
- `store-measurements.json`: dimensions in centimeters, including labels for inferred positions.

The center tables are omitted. The entrance orientation, shelf heights, cabinet bases, columns, racks, and fridges follow the supplied photos and measurements. Some small gaps and placement offsets remain inferred. Image uploads and shared admin publishing are not implemented yet.

The entrance glass is 8.5 m from the rear fridge/freezer door fronts. Their 60 cm depth extends beyond that distance, so the modeled shell is 9.1 m long. Other fixture distances from the entrance stay as measured.

## Run locally

Serve this folder so photo textures load correctly:

```sh
python -m http.server 8000
```

Then visit `http://localhost:8000/`.

## Deployment

GitHub Pages publishes the repository root from the `main` branch. The deployed viewer loads directly in the page. After editing the standalone export or renderer compatibility code, run `python source/prepare-desktop.py` to regenerate `index.html`, then commit and push.

To replace a shelf photo, update the corresponding JPEG in `assets/shelves/` and push it. The HTML sources reference these same files; photos are no longer embedded in the HTML. Keep the same framing and dimensions when replacing a photo, because the current crop and shelf-straightening settings were calibrated to the supplied images.

Store photographs and branding remain the property of their respective owners.
