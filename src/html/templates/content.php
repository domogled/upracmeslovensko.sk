<div class="container">
		<!-- Content -->
		<div class="content">
			<div class="container top" style="">
    <?php require 'banner.php'; ?>



    <?php require 'velke_menu_var_1.php'; ?>


            <?php require 'velke_menu_var_2.php'; ?>


            <?php require 'velke_menu_var_3.php'; ?>




    <script>
        $(function () {
            $(".block td.text-center").mouseover(function() {
                $(this).addClass("pulse");
            });
            $(".block td.text-center").mouseout(function() {
                $(this).removeClass("pulse");
            });

        });
    </script>
    <div class="block">


    <script>
        $(function () {
            var images= [
                "/_cachr/2b1d4a60a859f2124cfe1da5331ee230ce45d0d0.jpg",
                "/_cachr/215b8f42bd50f1fda209479acf2b55d6049e79fa.jpg",
                "/_cachr/cdd6242d54adb241570cfc98acaa7688bbe93dd5.jpg",
                "/_cachr/af83157f1df36376d1adb0ba5cda8ea2e4d86e2a.jpg",
                "/_cachr/4aa647569ad1b08f94155d698e62153cd566fe05.jpg",
                "/_cachr/da460025a2ba8e79934400989eb9ccfc8445f91d.jpg",
                "/_cachr/b5c5116154745ba4afc01b00d5dc7b520327dcba.jpg",
                "/_cachr/6a7fd945264356eb6adcb0fecba425c41340404a.jpg",
                "/_cachr/0c985335032eb3507a9f25df048ec5fa7eb55ef1.jpg",
                "/_cachr/aac4a8dd902b8c46e04cd7650bf24093da6059a0.jpg",
                "/_cachr/49ec4712a837a27255b014f4af712c9d83ec91be.jpg",
                "/_cachr/729081b78866616f6bdcf215a5026f20dcac704a.jpg",
                "/_cachr/109fb2bc1652e50b55b96499406cba32e4588310.jpg",
                "/_cachr/ca50f79ce709878b192440bf24831649920945c4.jpg",
                "/_cachr/aef64431ec03961378e328515cb09b58c970be64.jpg",
                "/_cachr/c50cf703da7420ff16da9660afe6fee5d6f721cb.jpg",
                "/_cachr/deeb93dfb6138e98183d52578be603167e3c926c.jpg",
                "/_cachr/2bebc0c5e50054fdaa1798c1610f7b9e9e1beb2e.jpg",
                "/_cachr/2ef39e8c9af4cd94aa2394cb37b8a938359fa9ec.jpg",
                "/_cachr/d2d8fd4ac9fba200e11cc5ff912f2565fe121c35.jpg",
                "/_cachr/31ecaa673827ab547fcaafea5cc4b58b03d58c4b.jpg",
                "/_cachr/bd97a737d52bcfdd515811a2e5a511ecfed5d6a9.jpg",
                "/_cachr/90dd9d37ab18167056a633c7f30da92f3052abca.jpg",
                "/_cachr/eafc62834a9aa15c6fcccef560365795eff03a71.jpg",
                "/_cachr/bc4d91f9b177dc96db402c6bcdbed444c806cc69.jpg",
                "/_cachr/3977c274ebb473247d77cda48be00fa6a69eaedd.jpg",
                "/_cachr/ead98b2e190d3c3bfdaa80364cda662d164b16f0.jpg",
                "/_cachr/e301031517ef8f9be7ec16c7fb6cefd897f5eac1.jpg",
                "/_cachr/f195e406517d6e6d374c987160713ab51f9860d1.jpg",
                "/_cachr/3c565eb9a4b4a7c7af828a510397c2265a645ed1.jpg",
                "/_cachr/d72f3edcc81107c552e903bad467669b82a4e6e7.jpg",
                "/_cachr/87425d0a7dc5d0a60e35c5298abb1470415bcc8e.jpg",
                "/_cachr/fb03715b62bf53400f1eb60798dc8cdd81438a49.jpg",
                "/_cachr/7b1e35017f1bcc791690d33dede00941a65b58bd.jpg",
                "/_cachr/a91d48e05a6b6055671e6f1885b191e23faa4f0f.jpg",
                "/_cachr/70a67a0d3a8717543134ab7a9a9fa18356e7e7e6.jpg",

                "/_cachr/fc8ce66f95506ddc5c73298e11f82047f0043f45.jpg",
                "/_cachr/69f928a5723d37e98705dc9aaa85a9915ee50b36.jpg",
                "/_cachr/c15fbba8809cfb3220035bdfb5c01e9c0af85419.jpg",
                "/_cachr/0e6f3609ccdeb1bd0deb265996ff5631c1dd1479.jpg",
                "/_cachr/99b70e0ccfe656fe24049b1dcf599b96e74e1991.jpg",
                "/_cachr/18cc35cae0ed3beb5999482633c5a565cf21d1b5.jpg",
                "/_cachr/1e75419dc06a97335568fbc7657536f980d699a7.jpg",
                "/_cachr/3f0e42cbababd17d2189554306de3bbae4a2fa83.jpg",
                "/_cachr/168a755c0dc2653a87d92ffd90a64d395b15c157.jpg",
                "/_cachr/aed00d1d50ae77a87a125914a00db3e0f111fb49.jpg",
                "/_cachr/78503671dfb84f74730fa6e0d571b26de16e9852.jpg",

                "/_cachr/7629feb463308827f0cbb87034ccdd185e566052.jpg",
                "/_cachr/f53476a5e1157394b2b339707da2f48c51b7f046.jpg",
                "/_cachr/d937ede406685de0175d5617d436e790eaf7df09.jpg",
                "/_cachr/f8279b4fad377d76716e5fea83b05bc91c19a63b.jpg",
                "/_cachr/1692e97b5fd85dbe163220c4949e78f9235486df.jpg",
                "/_cachr/0b562da58950b1985668ee3b5481c3fc87806e17.jpg",
                "/_cachr/a6a20d94d6f0f151615eb25409da4a6bbf18d37c.jpg",
                "/_cachr/08e2aaf2dfb15912ae1333c211bcd9ea04bace5e.jpg"





            ].sort(function() {
               return .5 - Math.random();
             });
            for(var i=0; i < images.length; i++) {
                $("#slideImages").append('<div><img u="image" src2="'+images[i].replace(/\/upload/g,"/upload/c_thumb,e_sharpen,h_220,w_400")+'" /></div>');
            }
        });
    </script>
    <script type="text/javascript" src="/scripts/jssor.slider.mini.js"></script>
    <script>
        jQuery(document).ready(function ($) {
            var options = { $AutoPlay: true };
            var jssor_slider1 = new $JssorSlider$('slider1_container', options);
        });
    </script>
    <div class="row">        
        <?php require 'foto_z_lonska.php'; ?>



        <?php require 'statistika_uklidu.php'; ?>

        <?php require 'soutez_musime_to_uklidit.php'; ?>


    </div>




        <div class="row">
            <?php require 'co_je_noveho.php'; ?>

            <?php require 'medialni_partneri.php'; ?>

            <?php require 'napsali_o_nas.php'; ?>

        </div>
        <!--
        <div class="row">
            <h3 class="text-center" style="line-height: 16px; padding-top: 16px; margin-top: 0px; margin-bottom: 20px;">Chcete nás podpořit?</h3>
            <div class="col-sm-4 col-sm-offset-2">
                <iframe
                    style="width:300px; height:300px; overflow: hidden; border-style:none; "
                    src="http://www.darujme.cz/dar/widgets/widget.php?widget=859">
                </iframe>
            </div>
            <div class="col-sm-4 text-center">
            <br />
            <a href="https://givt.cz/spolek-ekosmak" target="_blank"><img style="padding: 15px;" src="/_cachr/838476286c709986fc4daf32bbe0b3f5a8e776ba.png" /></a>
            <br /><em>Svým nákupem přes givt přispějete například na pevné pytle na odpad, které poputují dobrovolníkům připraveným přiložit ruku k dílu a přičinit se o čistší a krásnější Česko.</em>
            </div>
        </div>
        -->

    </div>
</div>
		</div>
		<!-- Footer -->
		<?php require 'content_footer_container.php'; ?>
<!-- /container -->
    <?php require 'generalni_partner.php'; ?>

    
<?php require 'kontakty.php'; ?>



<?php require 'spolufinancovan_MZP.php'; ?>

    
    <!-- Scripts -->
    <script defer src="/scripts/script.js"></script>

    <script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

      ga('create', 'UA-352014-31', 'auto');
      ga('send', 'pageview');

    </script>

	<div id="fb-root"></div>
        <script>(function(d, s, id) {
          var js, fjs = d.getElementsByTagName(s)[0];
          if (d.getElementById(id)) return;
          js = d.createElement(s); js.id = id;
          js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=124942087606035";
          fjs.parentNode.insertBefore(js, fjs);
        }(document, 'script', 'facebook-jssdk'));</script>
</div>
