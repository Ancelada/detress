var unit_module = {};

//блоки
unit_module.unit = $('.page_unit_content');

//функции


//события
unit_module.unit.on('click', function(){
	url = $(this)[0]['dataset']['id'];
	window.location = url;
});