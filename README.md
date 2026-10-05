# Shofankom 3D Store

Interactive, measured 3D walkthrough of the Shofankom store.

**[Open the walkthrough](https://samiandoni.github.io/shofankom-3d-store/)**

## Explore

- Drag to look around and use Forward / Back to move along the aisle.
- Scroll or use the zoom buttons to zoom.
- Select a photo section and inspect it up close.
- Switch to overview or plan to see the layout.

The walkthrough supports desktop and mobile browsers with WebGL. Viewer libraries are pinned and hosted in this repository, so no external CDN is required.

## Project files

- `index.html`: standalone browser walkthrough, including embedded store photo textures.
- `source/store-measured.html`: original editable model source.
- `source/standalone-export.html`: standalone export used by the deployment preparation script.
- `source/renderer-compat.js`: graphics initialization with a lower-resource retry and visible errors.
- `vendor/`: pinned Three.js and viewer resources, including their license notices.
- `store-measurements.json`: dimensions in centimeters, including labels for inferred positions.

The center tables are omitted. The entrance orientation, shelf heights, cabinet bases, columns, racks, and fridges follow the supplied photos and measurements. Some small gaps and placement offsets remain inferred. Image uploads and shared admin publishing are not implemented yet.

## Run locally

Open `index.html` in a browser, or serve this folder:

```sh
python -m http.server 8000
```

Then visit `http://localhost:8000/`.

## Deployment

GitHub Pages publishes the repository root from the `main` branch. The deployed viewer loads directly in the page. After editing the standalone export or renderer compatibility code, run `python source/prepare-desktop.py` to regenerate `index.html`, then commit and push.

Store photographs and branding remain the property of their respective owners.
