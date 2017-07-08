banner_module = {}
//переменные
banner_module.banner_units = banner_units;
banner_module.mobile_up_units = [];
//блоки


//функции
banner_module.toggle_active = toggleActive;


//***************
// функции
//***************



//***************
// события
//***************


function toggleActive(){
	if (menubar_module.vars.is_opened == false){
		$.each(banner_module.mobile_up_units, function(i){
			if (banner_module.mobile_up_units[i].active == true){

				banner_module.mobile_up_units[i]['html'].delay(200).fadeIn(200);

			} else {

				banner_module.mobile_up_units[i]['html'].fadeOut(200);			
			}
		});
	}
}

function ActiveNext(){
	$.each(banner_module.mobile_up_units, function(i){
		if (banner_module.mobile_up_units[i].active == true){
			current = banner_module.mobile_up_units[i];
			if (i == banner_module.mobile_up_units.length - 1){
				next = banner_module.mobile_up_units[0];
				current.active = false;
				next.active = true;
				return false;
			} else {
				next = banner_module.mobile_up_units[i+1];
				current.active = false;
				next.active = true;
				return false;
			}
		}
	});
	toggleActive();
}

function bannerInit(){

	$.each(banner_module.banner_units, function(i){
		banner_units[i]['html'] = $('.banner_item[data-id="'+banner_units[i]['id']+'"]');
	});

	if (menubar_module.mobile.screen == true){
		$.each($('.banner_mobile_up_unit'), function(i){
			banner_module.mobile_up_units.push({
				'html': $(this),
				'id': i,
				'children': [],
				'active': false,
			});	
		});
	}

	if (menubar_module.mobile.screen == true){
		//по 2 элемента в карусель
		no = 0;

		$.each(banner_module.mobile_up_units, function(j){
			
			$.each(banner_module.banner_units, function(i){

				i = no;

				if (banner_module.mobile_up_units[j].children.length < 2){
					if ($.inArray(
					banner_module.banner_units[i], banner_module.mobile_up_units[j].children, 0) == -1){

						banner_module.mobile_up_units[j].children.push(banner_module.banner_units[i]);
						no += 1;

					} else {

						return false;

					}
				}

			});

		});

		//перетаскиваем элементы внутрь dom карусели
		$.each(banner_module.mobile_up_units, function(i){
			parent = $(banner_module.mobile_up_units)[i];

			childs = $(banner_module.mobile_up_units)[i].children;

			$.each(childs, function(j){
				childs[j]['html'].detach().appendTo(parent['html']);
			});
		});

		//делаем активным первый элемент баннера
		banner_module.mobile_up_units[0].active = true;
		banner_module.toggle_active();

		var timerId = setInterval(ActiveNext, 10000);
	}
}


bannerInit();

console.log(banner_module.banner_units);
console.log(banner_module.mobile_up_units);