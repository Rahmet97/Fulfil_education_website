$(function () {
   $(".slider__slick").slick({
      centerMode: true,
      centerPadding: "60px",
      arrows: true,
      dots: true,
      slidesToShow: 3,
      // autoplay:true,
      speed: 800,
      autoplaySpeed: 1000,
      responsive: [
         {
            breakpoint: 865,
            settings: {
               centerMode: false,
               slidesToShow: 2,
            },
         },
         {
            breakpoint: 630,
            settings: {
               centerMode: false,
               slidesToShow: 1,
            },
         },
      ],
   });

	AOS.init();
	
	VANTA.GLOBE({
		el: "#footer",
		mouseControls: true,
		touchControls: true,
		gyroControls: false,
		minHeight: 200.00,
		minWidth: 200.00,
		scale: 1.00,
		scaleMobile: 1.00,
		backgroundColor: 0x18191b
	})

	VANTA.NET({
		el: "#about",
		mouseControls: true,
		touchControls: true,
		gyroControls: false,
		minHeight: 200.00,
		minWidth: 200.00,
		scale: 1.00,
		scaleMobile: 1.00,
		backgroundColor: 0x18191b
	})

	VANTA.RINGS({
		el: "#header-anime",
		mouseControls: true,
		touchControls: true,
		gyroControls: false,
		minHeight: 200.00,
		minWidth: 200.00,
		scale: 1.00,
		scaleMobile: 1.00,
		backgroundColor: 0x18191b
	})


});
