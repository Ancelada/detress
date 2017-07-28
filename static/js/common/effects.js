effects_module = {};

//блоки
effects_module.topbar = $('.topbar_wrapper');
effects_module.page_content = $('.page_content');
effects_module.login_modal = $('.login_modal_wrapper');

$('body').waitForImages(function() {

	effects_module.login_modal.delay(700).hide(400);

	console.log('All images have loaded.');

}, function(loaded, count, success) {

   console.log(
   	loaded + ' of ' + count + ' images has ' + (success ? 'loaded' : 'failed to load') +  '.');
   $(this).addClass('loaded');

});