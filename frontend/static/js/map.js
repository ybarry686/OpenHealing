
function embedMap(queryText, zoom) {
    const mapEl = document.getElementById("map");
    if (!mapEl) return;
  
    mapEl.innerHTML = `
      <iframe
        src="https://maps.google.com/maps?q=${encodeURIComponent(queryText)}&z=${zoom}&output=embed"
        width="100%"
        height="100%"
        style="border:0;"
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade">
      </iframe>
    `;
  }
  
  function renderDefaultMap() {
    embedMap("United States", 4);
  }
  
  function renderMap(resources, fallbackQuery) {
    const withCoords = (resources || []).filter(
      (r) => r.latitude != null && r.longitude != null
    );
  
    if (withCoords.length > 0) {
      const first = withCoords[0];
      embedMap(`${first.latitude},${first.longitude}`, 12);
      return;
    }
  
    if (fallbackQuery) {
      embedMap(fallbackQuery, 11);
      return;
    }
  
    renderDefaultMap();
  }