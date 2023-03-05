window.onload = function () {
	// Получаем все элементы со слайдерами
	var sliders_cmyk = document.getElementsByClassName("slider-cmyk");

	// Для каждого слайдера добавляем обработчик события input
	for (var i = 0; i < sliders_cmyk.length; i++) {
		sliders_cmyk[i].addEventListener("input", function() {
			// Получаем значение слайдера
			var sliderValue = this.value;

			// Получаем id поля ввода, связанного со слайдером
			var inputId = this.id.replace("slider-cmyk", "cmyk");

			// Находим соответствующее поле ввода и меняем его значение
			document.getElementById(inputId).value = sliderValue;
		});
	}

	var sliders_rgb = document.getElementsByClassName("slider-rgb");

	// Для каждого слайдера добавляем обработчик события input
	for (var i = 0; i < sliders_rgb.length; i++) {
		sliders_rgb[i].addEventListener("input", function() {
			// Получаем значение слайдера
			var sliderValue = this.value;

			// Получаем id поля ввода, связанного со слайдером
			var inputId = this.id.replace("slider-rgb", "rgb");

			// Находим соответствующее поле ввода и меняем его значение
			document.getElementById(inputId).value = sliderValue;
		});
	}

	var sliders_hls = document.getElementsByClassName("slider-hls");

	// Для каждого слайдера добавляем обработчик события input
	for (var i = 0; i < sliders_hls.length; i++) {
		sliders_hls[i].addEventListener("input", function() {
			// Получаем значение слайдера
			var sliderValue = this.value;

			// Получаем id поля ввода, связанного со слайдером
			var inputId = this.id.replace("slider-hls", "hls");

			// Находим соответствующее поле ввода и меняем его значение
			document.getElementById(inputId).value = sliderValue;
		});
	}
}

const sliders_cmyk = document.querySelectorAll('.slider-cmyk');
const colorBox_cmyk = document.querySelector('#color-box-cmyk');

function updateColor_cmyk() {
	console.log(sliders_cmyk[0].value)
	const c = sliders_cmyk[0].value / 100;
	const m = sliders_cmyk[1].value / 100;
	const y = sliders_cmyk[2].value / 100;
	const k = sliders_cmyk[3].value / 100;
	const r = 255 * (1 - c) * (1 - k)
	const g = 255 * (1 - m) * (1 - k)
	const b = 255 * (1 - y) * (1 - k)
	const color_cmyk = `rgb(${r}, ${g}, ${b})`;
	colorBox_cmyk.style.backgroundColor = color_cmyk;
}

sliders_cmyk.forEach(slider_cmyk => {
	slider_cmyk.addEventListener('input', updateColor_cmyk);
});

updateColor_cmyk();

const textInputs = document.querySelectorAll('.input-group');

function updateSliderValue(event) {
	const slider = event.target.parentElement.querySelector('.slider-cmyk');
	slider.value = event.target.value;
	updateColor_cmyk();
}

textInputs.forEach(textInput => {
	textInput.addEventListener('input', updateSliderValue);
});

function hexToCmyk(hexValue) {
	hexValue = hexValue.replace("#", "");
  // Конвертируем HEX в значения RGB
	var r = parseInt(hexValue.substring(0, 2), 16);
	var g = parseInt(hexValue.substring(2, 4), 16);
	var b = parseInt(hexValue.substring(4, 6), 16);

	// Приводим значения RGB к диапазону от 0 до 1
	var red = r / 255;
	var green = g / 255;
	var blue = b / 255;

	// Вычисляем значения CMYK
	var k = 1 - Math.max(red, green, blue);
	var c = (1 - red - k) / (1 - k);
	var m = (1 - green - k) / (1 - k);
	var y = (1 - blue - k) / (1 - k);

	// Приводим значения CMYK к диапазону от 0 до 100
	c = Math.round(c * 100);
	m = Math.round(m * 100);
	y = Math.round(y * 100);
	k = Math.round(k * 100);

	return [c, m, y, k];
}

function pic_cmyk(event){
	const colorPicker = new iro.ColorPicker("#color-picker-cmyk", {
		width:180, color: "#fff"
	});
	let hexValue;
	colorPicker.on('color:change', function (color) {
		hexValue = color.hexString;
		colorBox_cmyk.style.backgroundColor = hexValue;
		var array = hexToCmyk(hexValue);
		const c = array[0];
		const m = array[1];
		const y = array[2];
		const k = array[3];
		document.getElementById("slider-cmyk1").value = c;
		document.getElementById("slider-cmyk2").value = m;
		document.getElementById("slider-cmyk3").value = y;
		document.getElementById("slider-cmyk4").value = k;
		document.getElementById("cmyk1").value = c.toString();
		document.getElementById("cmyk2").value = m.toString();
		document.getElementById("cmyk3").value = y.toString();
		document.getElementById("cmyk4").value = k.toString();
		updateColor_cmyk()
	});
}

pic_cmyk()

const sliders_rgb = document.querySelectorAll('.slider-rgb');
const colorBox_rgb = document.querySelector('#color-box-rgb');

function updateColor_rgb() {
	const r = sliders_rgb[0].value;
	const g = sliders_rgb[1].value;
	const b = sliders_rgb[2].value;
	const color_rgb = `rgb(${r}, ${g}, ${b})`;
	colorBox_rgb.style.backgroundColor = color_rgb;
}

sliders_rgb.forEach(slider_rgb => {
	slider_rgb.addEventListener('input', updateColor_rgb);
});

updateColor_rgb();

const textInputs_rgb = document.querySelectorAll('.input-group');

function updateSliderValue_rgb(event) {
	const slider = event.target.parentElement.querySelector('.slider-rgb');
	slider.value = event.target.value;
	updateColor_rgb();
}

textInputs_rgb.forEach(textInput => {
	textInput.addEventListener('input', updateSliderValue_rgb);
});

function hexToRgb(hexValue) {
	hexValue = hexValue.replace("#", "");
  	// Конвертируем HEX в значения RGB
	var r = parseInt(hexValue.substring(0, 2), 16);
	var g = parseInt(hexValue.substring(2, 4), 16);
	var b = parseInt(hexValue.substring(4, 6), 16);

	return [r, g, b];
}

function pic_rgb(event){
	const colorPicker = new iro.ColorPicker("#color-picker-rgb", {
		width:180, color: "#fff"
	});
	let hexValue;
	colorPicker.on('color:change', function (color) {
		hexValue = color.hexString;
		colorBox_rgb.style.backgroundColor = hexValue;
		var array1 = hexToRgb(hexValue);
		const r = array1[0];
		const g = array1[1];
		const b = array1[2];
		document.getElementById("slider-rgb1").value = r;
		document.getElementById("slider-rgb2").value = g;
		document.getElementById("slider-rgb3").value = b;
		document.getElementById("rgb1").value = r.toString();
		document.getElementById("rgb2").value = g.toString();
		document.getElementById("rgb3").value = b.toString();
		updateColor_rgb()
	});
}

pic_rgb()

const sliders_hls = document.querySelectorAll('.slider-hls');
const colorBox_hls = document.querySelector('#color-box-hls');

function hue_to_rgb(p, q, t){
	if (t < 0){
		t += 1;
	}
	if (t > 1){
		t -= 1;
	}
	if (t < 1/6){
		return p + (q - p) * 6 * t;
	}
	if (t < 1 / 2){
		return q;
	}
	if (t < 2 / 3){
		return p + (q - p) * (2 / 3 - t) * 6;
	}
	return p;
}

function updateColor_hls() {
	let h = sliders_hls[0].value;
	const l = sliders_hls[1].value;
	const s = sliders_hls[2].value;
	h /= 360.0

	let r = 0;
	let g = 0;
	let b = 0;
	let p = 0;
	let q = 0;

        if (s == 0) {
			r = l;
			g = l;
			b = l;
		}
        else{
			if( l < 0.5){
				q = l * (1 + s)
			}
			else {
				q = l + s - l * s
			}
            p = 2 * l - q
            r = hue_to_rgb(p, q, h + 1 / 3)
            g = hue_to_rgb(p, q, h)
            b = hue_to_rgb(p, q, h - 1 / 3)
		}

		r *= 255;
		g *= 255;
		b *= 255;
	const color_hls = `rgb(${r}, ${g}, ${b})`;
	colorBox_hls.style.backgroundColor = color_hls;
}

sliders_hls.forEach(slider_hls => {
	slider_hls.addEventListener('input', updateColor_hls);
});

updateColor_hls();

const textInputs_hls = document.querySelectorAll('.input-group');

function updateSliderValue_hls(event) {
	const slider = event.target.parentElement.querySelector('.slider-hls');
	slider.value = event.target.value;
	updateColor_hls();
}

textInputs_hls.forEach(textInput => {
	textInput.addEventListener('input', updateSliderValue_hls);
});

function hexToHls(hex) {
  // Парсим цвет HEX в значения RGB
  const r = parseInt(hex.slice(1, 3), 16) / 255;
  const g = parseInt(hex.slice(3, 5), 16) / 255;
  const b = parseInt(hex.slice(5, 7), 16) / 255;

  // Вычисляем насыщенность
  const max = Math.max(r, g, b);
  const min = Math.min(r, g, b);
  let l = (max + min) / 2;
  let s = 0;

  if (max !== min) {
    s = l > 0.5 ? (max - min) / (2 - max - min) : (max - min) / (max + min);
  }

  // Вычисляем оттенок
  let h = 0;
  if (max === r && g >= b) {
    h = 60 * ((g - b) / (max - min));
  } else if (max === r && g < b) {
    h = 60 * ((g - b) / (max - min)) + 360;
  } else if (max === g) {
    h = 60 * ((b - r) / (max - min)) + 120;
  } else if (max === b) {
    h = 60 * ((r - g) / (max - min)) + 240;
  }

  // Округляем значения и возвращаем в формате HLS
  h = Math.round(h);
  s = Math.round(s * 100);
  l = Math.round(l * 100);

  return [h, l, s];
}


function pic_hls(event){
	const colorPicker = new iro.ColorPicker("#color-picker-hls", {
		width:180, color: "#fff"
	});
	let hexValue;
	colorPicker.on('color:change', function (color) {
		hexValue = color.hexString;
		colorBox_hls.style.backgroundColor = hexValue;
		var array2 = hexToHls(hexValue);
		const h = array2[0];
		const l = array2[1];
		const s = array2[2];
		document.getElementById("slider-hls1").value = h;
		document.getElementById("slider-hls2").value = l;
		document.getElementById("slider-hls3").value = s;
		document.getElementById("hls1").value = h.toString();
		document.getElementById("hls2").value = l.toString();
		document.getElementById("hls3").value = s.toString();
		updateColor_hls()
	});
}

pic_hls()
