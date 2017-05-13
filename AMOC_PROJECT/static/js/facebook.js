// initialize and setup facebook js sdk
		window.fbAsyncInit = function() {
		    FB.init({
		      appId      : '135721630293659',
		      xfbml      : true,
		      version    : 'v2.8'
		    });
		};

		(function(d, s, id){
		    var js, fjs = d.getElementsByTagName(s)[0];
		    if (d.getElementById(id)) {return;}
		    js = d.createElement(s); js.id = id;
		    js.src = "//connect.facebook.net/en_US/sdk.js";
		    fjs.parentNode.insertBefore(js, fjs);
		}(document, 'script', 'facebook-jssdk'));

		// login with facebook with extra permissions
		var ok=1;
		function login() {
			FB.login(function(response) {
				if (response.status === 'connected') {
		    		FB.api('/me', function(response) {
					document.getElementById('hid1').value = 'https://graph.facebook.com/' + response.id + '/picture';
					document.getElementById('hid2').value = response.name;
					document.getElementById('hid3').value = response.email;
					ok = 0;
				});
		    	}
			}, {scope: 'email'});
			if (ok === 0)
			{
				document.getElementById('myform').submit();
			};

		}
