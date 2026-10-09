// Google Earth Engine Script: Feature Extraction for Landslide Susceptibility
// Features extracted: Topography (Elevation, Slope) and NDVI

// Load Region of Interest (ROI) - Placeholder coordinates
var roi = ee.Geometry.Polygon(
  [[[90.0, 25.0], [93.0, 25.0], [93.0, 26.0], [90.0, 26.0]]]
);

// Load SRTM Digital Elevation Model (DEM)
var dem = ee.Image("USGS/SRTMGL1_003").clip(roi);
var elevation = dem.select('elevation');
var slope = ee.Terrain.slope(dem);

// Load Sentinel-2 for NDVI (Vegetation Index)
var s2 = ee.ImageCollection("COPERNICUS/S2_SR")
          .filterBounds(roi)
          .filterDate('2023-01-01', '2023-12-31')
          .median()
          .clip(roi);

var ndvi = s2.normalizedDifference(['B8', 'B4']).rename('NDVI');

// Combine all ML features into a single image
var predictors = elevation.addBands(slope).addBands(ndvi);

print("Predictor variables ready for extraction:", predictors);