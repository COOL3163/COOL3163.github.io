console.log("READY")

$(document).ready(function() {
    // Cache selectors
    var topMenu = $(".nav-list"),
        topMenuHeight = $(".links").outerHeight(), 
        // All list items
        menuItems = topMenu.find("a"),
        // Anchors corresponding to menu items
        scrollItems = menuItems.map(function() {
            var item = $($(this).attr("href"));
            if (item.length) { return item; }
        });

    // Bind click handler to menu items
    // so we can get a fancy scroll animation
    menuItems.click(function(e) {
        var href = $(this).attr("href"),
            offsetTop = href === "#" ? 0 : $(href).offset().top - topMenuHeight + 1;
        
        $('html, body').stop().animate({
            scrollTop: offsetTop
        }, 850);
        
        e.preventDefault();
    });

    // Bind to scroll
    $(window).scroll(function() {
        // Get container scroll position
        var fromTop = $(this).scrollTop() + topMenuHeight;

        // Get id of current scroll item
        var cur = scrollItems.map(function() {
            if ($(this).offset().top < fromTop)
                return this;
        });
        
        // Get the id of the current element
        cur = cur[cur.length - 1];
        var id = cur && cur.length ? cur[0].id : "";

        // added this so that it always activates at the top
        if ($(window).scrollTop() === 0) {
            id = "home";
        }

        // Set/remove active class
        menuItems.removeClass("active");
        if (id) {
            menuItems.filter("[href='#" + id + "']").addClass("active");
        }
    });
});