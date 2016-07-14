//ACT 
 
  var nsw_settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://www.eventbriteapi.com/v3/events/26020261302/ticket_classes/?token=YPSILX7EXQ5J2BMWUSYX",
    "method": "GET",
    "headers": {}
  }

  $.ajax(nsw_settings).done(function (data) {
    console.log(data);
    
    var content = "";
    
    for (i = 0; i < data['ticket_classes'].length; i++) {
	     
	    var ticket_left	=	data['ticket_classes'][i].quantity_total - data['ticket_classes'][i].quantity_sold;
    	
    	content += "<tr><td>ACT</td><td>" + data['ticket_classes'][i].name + "</td>" + "<td>" + data['ticket_classes'][i].quantity_sold + "</td>" + "<td>" + ticket_left + "</td>" + "<td>" + data['ticket_classes'][i].quantity_total + "</td>" + "<td>" + data['ticket_classes'][i].on_sale_status + "</td></tr>";
    	//console.log(data['ticket_classes'][i].name);
    
    }
    
    $(".act").replaceWith(content);
  
  });


//NSW

  var nsw_settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://www.eventbriteapi.com/v3/events/26016065753/ticket_classes/?token=YPSILX7EXQ5J2BMWUSYX",
    "method": "GET",
    "headers": {}
  }

  $.ajax(nsw_settings).done(function (data) {
    console.log(data);
    
    var content = "";
    
    for (i = 0; i < data['ticket_classes'].length; i++) {
	     
	    var ticket_left	=	data['ticket_classes'][i].quantity_total - data['ticket_classes'][i].quantity_sold;
    	
    	content += "<tr><td>NSW</td><td>" + data['ticket_classes'][i].name + "</td>" + "<td>" + data['ticket_classes'][i].quantity_sold + "</td>" + "<td>" + ticket_left + "</td>" + "<td>" + data['ticket_classes'][i].quantity_total + "</td>" + "<td>" + data['ticket_classes'][i].on_sale_status + "</td></tr>";
    	//console.log(data['ticket_classes'][i].name);
    
    }
    
    $(".nsw").replaceWith(content);
  
  });
  

//QLD

  var nsw_settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://www.eventbriteapi.com/v3/events/26020708640/ticket_classes/?token=YPSILX7EXQ5J2BMWUSYX",
    "method": "GET",
    "headers": {}
  }

  $.ajax(nsw_settings).done(function (data) {
    console.log(data);
    
    var content = "";
    
    for (i = 0; i < data['ticket_classes'].length; i++) {
	     
	    var ticket_left	=	data['ticket_classes'][i].quantity_total - data['ticket_classes'][i].quantity_sold;
    	
    	content += "<tr><td>QLD</td><td>" + data['ticket_classes'][i].name + "</td>" + "<td>" + data['ticket_classes'][i].quantity_sold + "</td>" + "<td>" + ticket_left + "</td>" + "<td>" + data['ticket_classes'][i].quantity_total + "</td>" + "<td>" + data['ticket_classes'][i].on_sale_status + "</td></tr>";
    	//console.log(data['ticket_classes'][i].name);
    
    }
    
    $(".qld").replaceWith(content);
  
  });
  

//SA

  var nsw_settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://www.eventbriteapi.com/v3/events/26020556184/ticket_classes/?token=YPSILX7EXQ5J2BMWUSYX",
    "method": "GET",
    "headers": {}
  }

  $.ajax(nsw_settings).done(function (data) {
    console.log(data);
    
    var content = "";
    
    for (i = 0; i < data['ticket_classes'].length; i++) {
	     
	    var ticket_left	=	data['ticket_classes'][i].quantity_total - data['ticket_classes'][i].quantity_sold;
    	
    	content += "<tr><td>SA</td><td>" + data['ticket_classes'][i].name + "</td>" + "<td>" + data['ticket_classes'][i].quantity_sold + "</td>" + "<td>" + ticket_left + "</td>" + "<td>" + data['ticket_classes'][i].quantity_total + "</td>" + "<td>" + data['ticket_classes'][i].on_sale_status + "</td></tr>";
    	//console.log(data['ticket_classes'][i].name);
    
    }
    
    $(".sa").replaceWith(content);
  
  });
  

//TAS

  var nsw_settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://www.eventbriteapi.com/v3/events/26020202125/ticket_classes/?token=YPSILX7EXQ5J2BMWUSYX",
    "method": "GET",
    "headers": {}
  }

  $.ajax(nsw_settings).done(function (data) {
    console.log(data);
    
    var content = "";
    
    for (i = 0; i < data['ticket_classes'].length; i++) {
	     
	    var ticket_left	=	data['ticket_classes'][i].quantity_total - data['ticket_classes'][i].quantity_sold;
    	
    	content += "<tr><td>TAS</td><td>" + data['ticket_classes'][i].name + "</td>" + "<td>" + data['ticket_classes'][i].quantity_sold + "</td>" + "<td>" + ticket_left + "</td>" + "<td>" + data['ticket_classes'][i].quantity_total + "</td>" + "<td>" + data['ticket_classes'][i].on_sale_status + "</td></tr>";
    	//console.log(data['ticket_classes'][i].name);
    
    }
    
    $(".tas").replaceWith(content);
  
  });
  

//VIC

  var nsw_settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://www.eventbriteapi.com/v3/events/26184031142/ticket_classes/?token=YPSILX7EXQ5J2BMWUSYX",
    "method": "GET",
    "headers": {}
  }

  $.ajax(nsw_settings).done(function (data) {
    console.log(data);
    
    var content = "";
    
    for (i = 0; i < data['ticket_classes'].length; i++) {
	     
	    var ticket_left	=	data['ticket_classes'][i].quantity_total - data['ticket_classes'][i].quantity_sold;
    	
    	content += "<tr><td>VIC</td><td>" + data['ticket_classes'][i].name + "</td>" + "<td>" + data['ticket_classes'][i].quantity_sold + "</td>" + "<td>" + ticket_left + "</td>" + "<td>" + data['ticket_classes'][i].quantity_total + "</td>" + "<td>" + data['ticket_classes'][i].on_sale_status + "</td></tr>";
    	//console.log(data['ticket_classes'][i].name);
    
    }
    
    $(".vic").replaceWith(content);
  
  });
  

//WA

  var nsw_settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://www.eventbriteapi.com/v3/events/26020623385/ticket_classes/?token=YPSILX7EXQ5J2BMWUSYX",
    "method": "GET",
    "headers": {}
  }

  $.ajax(nsw_settings).done(function (data) {
    console.log(data);
    
    var content = "";
    
    for (i = 0; i < data['ticket_classes'].length; i++) {
	     
	    var ticket_left	=	data['ticket_classes'][i].quantity_total - data['ticket_classes'][i].quantity_sold;
    	
    	content += "<tr><td>WA</td><td>" + data['ticket_classes'][i].name + "</td>" + "<td>" + data['ticket_classes'][i].quantity_sold + "</td>" + "<td>" + ticket_left + "</td>" + "<td>" + data['ticket_classes'][i].quantity_total + "</td>" + "<td>" + data['ticket_classes'][i].on_sale_status + "</td></tr>";
    	//console.log(data['ticket_classes'][i].name);
    
    }
    
    $(".wa").replaceWith(content);
    
    $('.table-fixed-header').fixedHeader();
  
  });
  
  (function($) {

  	$.fn.fixedHeader = function (options) {
 		var config = {
 			topOffset: 40,
 			bgColor: '#EEEEEE'
 		};
 
 		
 		if (options){ $.extend(config, options); }

 		return this.each( function() {
 	
	 		var o = $(this);
	
	 		var $win = $(window)
	 		, $head = $('thead.header', o)
	 		, isFixed = 0;
	  
	 		var headTop = $head.length && $head.offset().top - config.topOffset;
	
	 		function processScroll() {
	 		
	 			if (!o.is(':visible')) return;
	 			
	 			var i, scrollTop = $win.scrollTop();
	 			
	 			var t = $head.length && $head.offset().top - config.topOffset;
	    
	 			if (!isFixed && headTop != t) { headTop = t; }
	    
	 			if      (scrollTop >= headTop && !isFixed) { isFixed = 1; }
	    
	 			else if (scrollTop <= headTop && isFixed) { isFixed = 0; }
	    
	 			isFixed ? $('thead.header-copy', o).removeClass('hide')
	            	: $('thead.header-copy', o).addClass('hide');
	  
	  		}
	  
	  		$win.on('scroll', processScroll);
	
	  		// hack sad times - holdover until rewrite for 2.1
	  		$head.on('click', function () {
	  			if (!isFixed) setTimeout(function () {  $win.scrollTop($win.scrollTop() - 47) }, 10);
	  		})
	
	  		$head.clone().removeClass('header').addClass('header-copy header-fixed').appendTo(o);
	  
	  		var ww = [];
	  		
	  		o.find('thead.header > tr:first > th').each(function (i, h){
	  		
	  			ww.push($(h).width());
	  	
	  		});
	  
	  		$.each(ww, function (i, w){
	  		
	  			o.find('thead.header > tr > th:eq('+i+'), thead.header-copy > tr > th:eq('+i+')').css({width: w});
	  	
	  		});
	
	  		
	  		o.find('thead.header-copy').css({ margin:'0 auto',
	                                 	width: o.width(),
	                                   'background-color':config.bgColor });
									   processScroll();
 		});
	};

})(jQuery);