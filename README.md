# Shofankom 3D Store

Interactive, measured 3D walkthrough of the Shofankom store.

**[Open the walkthrough](https://samiandoni.github.io/shofankom-3d-store/)**

## Explore

- On mobile, use the left thumb joystick to walk and drag the view with your other thumb to look around. Release the joystick to stop.
- On desktop, drag to look around and use arrow keys, WASD, or Forward / Back to move along the aisle.
- Scroll or use the zoom buttons to zoom.
- Select a photo section and inspect it up close.
- Switch to overview or plan to see the layout.

The walkthrough supports desktop and mobile browsers with WebGL. An internet connection is required for the pinned Three.js library and viewer resources.

## Project files

- `index.html`: standalone browser walkthrough, including embedded store photo textures.
- `source/store-measured.html`: editable model source before the standalone viewer wrapper.
- `store-measurements.json`: dimensions in centimeters, including labels for inferred positions.

The center tables are omitted. The entrance orientation, shelf heights, cabinet bases, columns, racks, and fridges follow the supplied photos and measurements. Some small gaps and placement offsets remain inferred. Image uploads and shared admin publishing are not implemented yet.

## Run locally

Open `index.html` in a browser, or serve this folder:

```sh
python -m http.server 8000
```

Then visit `http://localhost:8000/`.

## Deployment

GitHub Pages publishes the repository root from the `main` branch. Push an updated `index.html` to deploy a new version. Changes to the editable source must also be incorporated into `index.html` before pushing.

Store photographs and branding remain the property of their respective owners.
