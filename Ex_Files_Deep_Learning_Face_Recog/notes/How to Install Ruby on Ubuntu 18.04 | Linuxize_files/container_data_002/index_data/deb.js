var toEndFrame = false;

//Start Loader
setTimeout(function(){
  TweenLite.set(loader, {css:{'display' : 'block', 'transformOrigin' : '50% 50%'}});  
  TweenLite.to(loader, 16, {css:{'rotation' : '4500'}});  
},250);

//Load Images
function loadImages(){

	var adImages = [ "images/background.jpg", "images/orange_background.png", "images/logo.png", "images/text_1.png", "images/cta.png" ]
                     
	var adDivs = [ background, orange_background, logo, text_1, cta ]

                
	var i;
	var adImagesObject = [];
	var numberImagesLoaded = 0;
  
  var numberOfImages = adImages.length;
	
	for (i = 0; i < adImages.length; i++) {
		adImagesObject[i] = new Image();
		adImagesObject[i].src = adImages[i];
		adImagesObject[i].onLoad = onImageLoad();
	};
	
	function onImageLoad(){
		TweenLite.to(adDivs[i], 0, {css:{'background-image': 'url("'+ adImages[i] +'")' }});
		numberImagesLoaded++;
		if (numberImagesLoaded == numberOfImages) {
      TweenLite.to(loader, .4, {css:{'opacity' : '0'}, ease:Expo.easeOut});
      setAnimationQues();
			setTimeout(removeLoader, 300);
		};
	};
};


//Remove Loader
function removeLoader(){
   startAnimation();
};

function setAnimationQues(){
    TweenLite.set(background, {css:{'opacity' : '0', 'scale' : '1.2' }} )
    TweenLite.set(orange_background, {css:{'opacity' : '0', 'height' : '0' }} )
    TweenLite.set(logo, {css:{'left' : '-250px'}} )
    TweenLite.set(text_1, {css:{'height' : '36px', 'y' : '-10'}} ) 
    TweenLite.set(cta, {css:{'opacity' : '0'}} )
}



function startAnimation(){
    TweenLite.to(background, 1.5, {css:{'opacity' : '1'}, ease:Power2.easeOut});
    TweenLite.to(background, 4, {css:{'scale' : '1'}, ease:Power2.easeOut});
    
    setTimeout(function(){
      TweenLite.to(logo, 1.2, {css:{'x' : '250'}, ease:Expo.easeOut, delay: .7});
      TweenLite.to(orange_background, 1.3, {css:{'height' : '174px', 'opacity' : '1'}, ease:Expo.easeOut, delay: 1.5});
      TweenLite.to(text_1, 2.5, {css:{'height' : '146px', 'y' : '0'}, ease:Expo.easeOut, delay: 2}); 
      TweenLite.to(cta, 1.2, {css:{'opacity' : '1'}, ease:Expo.easeOut, delay: 3.2});
      
      TweenLite.to(cta, .8, {css:{'x' : '3'}, ease:Expo.easeOut, delay: 4});
      TweenLite.to(cta, .8, {css:{'x' : '0'}, ease:Expo.easeOut, delay: 4.7});
    },500);

   setTimeout(function(){
        toEndFrame = true;
      },3600);
}

function ctaOver(){
  if(toEndFrame){
      TweenLite.to(cta, .7, {css:{'x' : '3'}, ease:Expo.easeOut});
  }
}

function ctaOut(){
    TweenLite.to(cta, .7, {css:{'x' : '0'}, ease:Expo.easeOut});
}


function ctaExit(){
  
}

function ctaBg(){
  
}

setTimeout(loadImages, 250);