if (typeof gallery_array != 'undefined'){

	gallery_module = {};
	
	//переменные
	gallery_module.array = gallery_array;
	gallery_module.containers = $('.gallery_bucket');
	//блоки

	//функции

	function gallery_module_init(){
		//прикрерляем контейнеры
		$.each(gallery_module.containers, function(i){
			$.each(gallery_module.array, function(j){
				if ('container' in gallery_module.array[j] == false){
					gallery_module.array[j]['container'] = gallery_module.containers[i];
					return false;
				}
			});
		});

		$.each(gallery_module.array, function(j){
			gallery_module.array[j]['photoes'][0]['html'].appendTo(gallery_module.array[j]['container']);
		});
	}

	gallery_module_init();

	console.log(gallery_module.array);
}