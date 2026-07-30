# 5. Assets, Inspections, and Locations

## 5.1 Asset

An Asset may be a building, bridge, tunnel, roadway, utility, tower, industrial facility, transit asset, site, system, space, component, or other constructed asset. `assetType` is a vocabulary term rather than a closed mandatory enumeration. Assets may be nested through `parentId`.

## 5.2 Inspection Program

An Inspection Program groups recurring or related inspection events. It may reference inspection profiles, contracts, regulations, owner programs, or maintenance cycles.

## 5.3 Inspection Event

An Inspection Event defines a bounded occurrence with an asset, time range, participants, scope, status, and optional program. It may include field collection, desk review, automated processing, professional review, or combinations of these activities.

## 5.4 Location

A record may reference multiple locations. Examples include an asset path plus a drawing coordinate and an image polygon.

Drawing and image coordinates SHOULD be normalized decimal coordinates from `0` to `1`, measured from the source's top-left corner with positive X to the right and positive Y downward unless a profile explicitly states otherwise. Source dimensions, drawing revision, page or sheet, and geometry type SHOULD be supplied.

Geographic geometry follows GeoJSON-style coordinate ordering. Implementations should not infer a coordinate reference system other than the one explicitly stated or required by the relevant profile.
