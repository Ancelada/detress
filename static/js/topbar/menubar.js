menubar_module = {}
//блоки
menubar_module.menubar_item_line = $('.menubar_item_line');
menubar_module.triangle = $('.menubar_item_triangle_wrapper');
menubar_module.menu_content_wrapper = $('.menubar_item_content_wrapper');
menubar_module.menu_content = $('.menubar_item_content');

menubar_module.mobile = {};
menubar_module.mobile.close = $('.mobile_close');
menubar_module.mobile.menubar_wrapper = $('.menubar_wrapper');
menubar_module.mobile.open = $('.mobile_menu_button_ico');
menubar_module.mobile.back = $('.menubar_back');
//функции
menubar_module.init = menubarInit;

//переменные
menubar_module.vars = {};
menubar_module.vars.units = menubar_units;

var triangle;
var text;

//*************************
// события
//*************************
//вернуться на первый уровень меню для мобильника
menubar_module.mobile.back.on('click', function(){
	menubar_module.menu_content_wrapper.hide(200);
})

//показать для мобильника
menubar_module.mobile.open.on('click', function(){
	menubar_module.mobile.menubar_wrapper.show(200);
});

//срыть для мобильника
menubar_module.mobile.close.on('click', function(){
	menubar_module.mobile.menubar_wrapper.hide(400);
});

//наводим курсор на заголовок меню
menubar_module.menubar_item_line.on('mouseover', function(){
	menubar_module.menu_content_wrapper.show();

	unit_id = parseInt($(this).attr('data-id'));
	showContent(unit_id);

	if (triangle){
		triangle.hide();
	}

	triangle = $(this).find('.menubar_item_triangle_wrapper');
	triangle.show();
});

menubar_module.menu_content.on('mouseleave', function(){
	menubar_module.menu_content_wrapper.hide();
	triangle.hide();
});



function showContent(unit_id){
	$.each(menubar_module.vars.units, function(key, value){
		if (value['id'] == unit_id){
			value['header_content_html'].show();
		} else {
			value['header_content_html'].hide();
		}
	});
}


function menubarInit(){

	html_item_lines = $('.menubar_item_line');

	html_item_content = $('.menubar_item_content');

	//соединяем html заголовки меню
	//соединяем панели контента html с заголовками меню
	$.each(menubar_module.vars.units, function(i){
		item = menubar_module.vars.units[i];
		item_id = menubar_module.vars.units[i]['id'];

		item['header_html'] = $('.menubar_item_line[data-id="'+item_id+'"]');

		item['header_content_html'] = $('.menubar_item_content[data-id="'+item_id+'"]');



	});
}

menubar_module.init();

console.log(menubar_module.vars.units);