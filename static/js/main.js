const greather = 1.5; // modificador de tamaño para la seccion de poderes

// seleccion de poderes por id para tomar el valor del div que retorna la API
const intelligence = document.getElementById('intelligence');
const strength = document.getElementById('strength');
const speed = document.getElementById('speed');
const durability = document.getElementById('durability');
const power = document.getElementById('power');
const combat = document.getElementById('combat');
const btn_search = document.getElementById('btn_search');
const name = document.getElementById('name');


// seleciona el div del poder para modificar su estilo mediante css
const stats_intelligence = document.getElementById('stats_intelligence');
const stats_strength = document.getElementById('stats_strength');
const stats_speed = document.getElementById('stats_speed');
const stats_durability = document.getElementById('stats_durability');
const stats_power = document.getElementById('stats_power');
const stats_combat = document.getElementById('stats_combat');


// SECCION DE ASIGNACION DE COLORES Y TAMAÑOS A LOS DIV DE PODERES
stats_intelligence.style.backgroundColor = `#009FFD`;
stats_intelligence.style.width = `${intelligence.innerText*greather}px`; // asigna el valor del div al alto
stats_intelligence.style.height = `${intelligence.innerText*greather}px`; 


stats_strength.style.backgroundColor = `#8D0801`;
stats_strength.style.width = `${strength.innerText*greather}px`;
stats_strength.style.height = `${strength.innerText*greather}px`;

stats_speed.style.backgroundColor = `#f45e00`;
stats_speed.style.width = `${speed.innerText*greather}px`;
stats_speed.style.height = `${speed.innerText*greather}px`;

stats_durability.style.backgroundColor = `#553739`;
stats_durability.style.width = `${durability.innerText*greather}px`;
stats_durability.style.height = `${durability.innerText*greather}px`;

stats_power.style.backgroundColor = `#2C6E49`;
stats_power.style.width = `${power.innerText*greather}px`;
stats_power.style.height = `${power.innerText*greather}px`;

stats_combat.style.backgroundColor = `#EE2E31`;
stats_combat.style.width = `${combat.innerText*greather}px`;
stats_combat.style.height = `${combat.innerText*greather}px`;
