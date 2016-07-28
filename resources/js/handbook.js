/** For portal.govhack.org/handbook **/
var HB = (function(){
    'use strict';
    
    var self = {};
    self.enableSidebarDrag = enableSidebarDrag;
    self.groupHeadings = groupHeadings;
    self.collapsePageContent = collapsePageContent;
    self.updateSelectedLocation = updateSelectedLocation;
    self.storage = new handbookStorage();
    return self;
    
    /** 
     * Specifically, make the sidebar variable in width
     */
    function enableSidebarDrag(selectorSidebar, selectorMain){
        
        if (!selectorSidebar) throw 'Argument 1 must be a CSS selector';
        if (!selectorMain) throw 'Argument 2 must be a CSS selector';
        
        var elemSidebar = document.querySelector(selectorSidebar); 
        var elemMain = document.querySelector(selectorMain);
        
        elemSidebar.addEventListener('click', function init() {
            elemSidebar.removeEventListener('click', init, false);
            elemSidebar.className = elemSidebar.className + ' resizable';
            var resizer = document.createElement('div');
            resizer.className = 'resizer-handle';
            elemSidebar.appendChild(resizer);
            resizer.addEventListener('mousedown', initDrag, false);
        }, false);

        var startX, sidebarStartWidth, mainStartLeft;
        var sidebarMinWidth, sidebarMaxWidth;
        // var startY, startHeight;

        function initDrag(e) {
            startX = e.clientX;
            // startY = e.clientY;
            sidebarStartWidth = parseInt(document.defaultView.getComputedStyle(elemSidebar).width, 10);
            sidebarMinWidth = parseInt(document.defaultView.getComputedStyle(elemSidebar).minWidth, 10);
            sidebarMaxWidth = parseInt(document.defaultView.getComputedStyle(elemSidebar).maxWidth, 10);
            mainStartLeft = parseInt(document.defaultView.getComputedStyle(elemMain).left, 10);
            // startHeight = parseInt(document.defaultView.getComputedStyle(elemSidebar).height, 10);
            document.documentElement.addEventListener('mousemove', doDrag, false);
            document.documentElement.addEventListener('mouseup', stopDrag, false);
        }

        function doDrag(e) {
            var isAboveMin = sidebarStartWidth + e.clientX - startX > sidebarMinWidth;
            var isBelowMax = sidebarStartWidth + e.clientX - startX < sidebarMaxWidth;
            if (isAboveMin && isBelowMax){
                elemSidebar.style.width = (sidebarStartWidth + e.clientX - startX) + 'px';
                elemMain.style.left = (mainStartLeft + e.clientX - startX) + 'px';                
            }
            // elemSidebar.style.height = (startHeight + e.clientY - startY) + 'px';
        }

        function stopDrag(e) {
            document.documentElement.removeEventListener('mousemove', doDrag, false);
            document.documentElement.removeEventListener('mouseup', stopDrag, false);
        }
    }
    
    /**
     * Implements a grouping spec as per what our collapse plugin expects:
     * https://github.com/danielstocks/jQuery-Collapse#usage
     * 
     * @param jQuery element
     */
    function groupHeadings($elem, headingTagNames){
        
        if (!$elem) throw 'No jQuery element was provided in argument 1';
        headingTagNames = headingTagNames || ['h1', 'h2'];

        var $shadow = $('<div>');
        var $subcontent = $('<div>');
        $elem.children().each(function(){
            var $this = $(this);
            var tagName = $this.prop('tagName').toLowerCase();
            if (~headingTagNames.indexOf(tagName)){
                // Wrap up the old one, push it into shadow.
                $this.addClass('heading-toggle');
                $subcontent.clone().appendTo($shadow);
                $this.clone().appendTo($shadow);
                $subcontent = $('<div>');
            }
            else {
                $this.appendTo($subcontent);
            }
        });
        if ($subcontent){
            $subcontent.clone().appendTo($shadow);
        }
        // Switcharoo
        $elem.empty();
        $shadow.children().appendTo($elem);
        // delete $shadow;
    }
    
    /**
     * An IO class for localStorage (or could be made into 
     * a adapter, later down the track)
     */
    function handbookStorage(){
        
        if (!window.localStorage){
            console.warn('No localstorage');
            return;
        }
        this.get = function(key){
            return window.localStorage.getItem(lsk(key));
        }
        this.set = function(key, value){
            window.localStorage.setItem(lsk(key), value);
        }
        
        //========================
        
        var locationIdKey = 'event_gid';
        var locationNameKey = 'event_name';
        this.hasLocation = function(){
            return !!window.localStorage.getItem(lsk(locationIdKey));
        }
        this.getLocation = function(locationLoadedCallback){
            var id = window.localStorage.getItem(lsk(locationIdKey));
            var name = window.localStorage.getItem(lsk(locationNameKey));
            var location = {
                id: id,
                name: name
            };
            retrieveLocationApi(id).done(function(data){
                $.extend(location, data || {});
                (locationLoadedCallback || $.noop)(location);
            });
            return location;
        }
        this.setLocation = function(values){
            if (typeof values === 'string'){
                var id = values;
                values = { id: id };
            }
            // if (!values.gid) throw 'Argument 1 must be an object that contains field `gid`';
            // values = $.extend({ 
                // gid: 'sydney',
                // name: 'sydney'
            // }, values || {});
            window.localStorage.setItem(lsk(locationIdKey), values.id);
            window.localStorage.setItem(lsk(locationNameKey), values.name);
        }
        
        // Alias
        this.hasVenue = this.hasLocation;
        this.getVenue = this.getLocation;
        this.setVenue = this.setLocation;
        
        
        //========================
        
        function lsk(key){
            var localStorageKey = 'govhackhandbook';
            return [localStorageKey, key].join('_');
        }
        
        function retrieveLocationApi(locationId){
            // returns a promise with .done(), .fail() and .always()
            var $prom = $.get('/feed/locations/all.json');
            if (locationId){
                return $prom.then(function(data){
                    if ($.isArray(data)){
                        return data.find(function(location){
                            return location.id === locationId;
                        });
                    }
                    return data;
                });
            }
            return $prom;
        }

    }
    
    /**
     * A standardised collapser function
     *
     * @param jQuery  A jQuerified element
     * @param Object  See the $.extend for the default opts
     */
    function collapsePageContent($collapseTargetParent, opts){
        if (!$collapseTargetParent) throw 'Must provide parent element as argument 1';

        if (HB.storage.get('show_sections_expanded') === 'yes'){
            console.warn('User has opted out of accordions');
            return;
        }

        opts = $.extend({
            validHeadingTags: ['h1', 'h2', 'h3'],
            headingThreshold: 3
        }, opts || {});
        
        if ($collapseTargetParent.find(opts.validHeadingTags.join(', ')).length >= opts.headingThreshold){

            // Groupify everything into heading+content pairs then
            // run el collapso https://github.com/danielstocks/jQuery-Collapse

            groupHeadings($collapseTargetParent, opts.validHeadingTags);

            $collapseTargetParent.collapse({
                query: opts.validHeadingTags.join(', '),
                persist: true,
                open: function(){
                    this.slideDown(100);
                },
                close: function(){
                    this.slideUp(100);
                }
            });

        }
        
    }
    
    
    function updateSelectedLocation(labelPrefix){
        labelPrefix = labelPrefix || '#custom-location';
        // Show customised event name
        var $customLocationNames = $(labelPrefix + '-name-help').add(labelPrefix + '-sidebar-button-label');
        var $customLocationFullNames = $(labelPrefix + '-sidebar-label');
        var $customLocationSection = $(labelPrefix + '-selected');
        var $customLocationHelpTable = $(labelPrefix + '-help-table');
        var $customLocationTableHelp = $(labelPrefix + '-table-help');
        if (HB.storage.getLocation().id){
            var event = HB.storage.getLocation(function(){
                if (event.name){
                    $customLocationNames.text(event.name);
                    $customLocationFullNames.text([(event.prefix || ''), event.name, (event.type ? '('+event.type+')' : '')].join(' '));
                }
                $customLocationSection.addClass('custom-event-selected');
                if (event.venue){
                    $customLocationHelpTable.show();
                    if (event.venue.host){
                        var $trHost = $('<tr>');
                        $trHost.append('<td>Host</td>');
                        $trHost.append('<td>'+event.venue.host+'&nbsp;&nbsp;</td>');
// <small><a href="'++'">'+email+'</a></small>
                        $trHost.appendTo($customLocationHelpTable.find('tbody'));
                    }
                    if (event.venue.team){
                        var $trTeam = $('<tr>');
                        $trTeam.append('<td>Team</td>');
                        $trTeam.append('<td>'+event.venue.team+'&nbsp;&nbsp;</td>');
                        $trTeam.appendTo($customLocationHelpTable.find('tbody'));
                    }

                    ['friday', 'saturday', 'sunday'].forEach(function(dayName){
                        var $trDay = $('<tr>');
                        $trDay.append('<td>'+dayName.charAt(0).toUpperCase()+dayName.slice(1)+' times</td>');
                        $trDay.append('<td>'+event.times[dayName].open+' to '+event.times[dayName].close+'</td>');
                        $trDay.appendTo($customLocationHelpTable.find('tbody'));
                    });

                    // if (event.times.friday){
                        // var $trFriday = $('<tr>');
                        // $trFriday.append('<td>Friday times</td>');
                        // $trFriday.append('<td>'+event.times.friday.open+' to '+event.times.friday.close+'</td>');
                        // $trFriday.appendTo($customLocationHelpTable);
                    // }
                    // if (event.times.saturday){
                        // var $trSaturday = $('<tr>');
                        // $trSaturday.append('<td>Saturday times</td>');
                        // $trSaturday.append('<td>'+event.times.saturday.open+' to '+event.times.saturday.close+'</td>');
                        // $trSaturday.appendTo($customLocationHelpTable);
                    // }
                    // if (event.times.sunday){
                        // var $trSunday = $('<tr>');
                        // $trSunday.append('<td>Sunday times</td>');
                        // $trSunday.append('<td>'+event.times.sunday.open+' to '+event.times.sunday.close+'</td>');
                        // $trSunday.appendTo($customLocationHelpTable);
                    // }
                }
            });
        }
        else {
            $sidebarLocationLabel.text($sidebarLocationLabel.data('originalLabel'));
            $customLocationSection.removeClass('custom-event-selected');
        }
    }
    
}());