<div class="banner">
        <div class="row">
            <div class="col-sm-12 col-md-6 col-xs-12 text-center center-block" style="margin-bottom: 25px; padding-left: 55px;">
                <a href="/"><img src="/images/2016/USUC_logo_inverse.png" class="img-responsive" style="margin-top: 2px; margin-bottom: 15px;
                margin-left: auto; margin-right: auto;"></a>
                <div style="font-size: 1.3em; font-weight: bold; margin-top: 45px; margin-bottom: 5px;">Hlavní úklidový den bude
                 <br>v sobotu 8. dubna 2017.<br>
              <!--Některé úklidy se pro vás ale stále chystají.<br />Najdete je v Mapě úklidů.-->
                                </div>
                <!--
               <div style="font-size: 1.3em; font-weight: bold; margin-top: 15px; margin-bottom: 5px;">Největší dobrovolnická akce v České republice<br />
                se uskuteční především v sobotu 16. dubna 2016,<br />
                uklízí se však i v jiných termínech
                </div>
                -->
<script>
    var hodin = 0;
    var hodinAct = 0;
    var uklidu = 0;
    var ukliduAct = 0;
    var chystanych = 0;
    var chystanychAct = 0;
    $(function () {
        function str2box(str) {
            str = str.toString();
            out = "";
            for(var i=0; i < str.length; i++) {
                out = out + '<span class="countBox">'+str[i]+'</span>';
            }
            return out;
        }
        hodin = Math.floor((Date.parse('Apr 16 2016 9:00') - Date.parse(new Date()))/(1000*60*60));
        setTimeout(function(){ countHodin(); }, 0);
        function countHodin() {
            if(hodinAct >= 5) {
                $("#countdown").html("Do začátku akce zbývá<br /> "+str2box(hodinAct)+" hodin");
            } else if(hodinAct >= 2) {
                $("#countdown").html("Do začátku akce zbývají<br /> "+str2box(hodinAct)+" hodiny");
            } else if(hodinAct == 1) {
                $("#countdown").html("Do začátku akce zbývá<br />jedna hodina");
            } else {
                //$("#countdown").html("Akce již proběhla.");
            }
            hodinAct++;
            if(hodinAct <= hodin) {
                setTimeout(function(){ countHodin(); }, 20);
            }
        }
        function countUklidu() {
            ukliduAct++;
            //$("#pocetUklidu").html("<br />Úklidů se letos zaregistrovalo již<br />"+str2box(ukliduAct)+"<br />Zaregistrujte i ten Váš!");
            if(ukliduAct < uklidu) {
                setTimeout(function(){ countUklidu(); }, 10);
            }
        }
        function countChystanych() {
            chystanychAct++;
            $("#countdown").html("Zaregistrováno je již <br />"+str2box(ukliduAct)+"<br /> úklidů");
            if(chystanychAct < chystanych) {
                setTimeout(function(){ countChystanych(); }, 10);
            }
        }
        $.getJSON( "http://www.uklidmecesko.cz/api/uklidyStatistika", {
                format: "json",
                cache: true
           }).done(function( results ) {
                if(results.hasOwnProperty("uklidu")) {
                    uklidu = results.uklidu;
                    chystanych = results.chystanych;
                    setTimeout(function(){ countUklidu(); }, 0);
                    setTimeout(function(){ countChystanych(); }, 0);
                }
           });
    });
</script>
            </div>

            <div class="col-md-3 hidden-sm hidden-xs">
                <div style="font-size: 1.1em; font-weight: bold; margin-top: 45px; margin-bottom: 0px; color: #ffffff; text-align: center; line-height: 2.2em;">
<span id="countdown"></span><span id="pocetUklidu"></span>
</div>
            </div>
            <div class="col-sm-6 col-md-3 col-xs-8 col-xs-offset-2 col-sm-offset-3 col-md-offset-0">
                <div class="flex-video thumbnail" style="margin: 0 auto; text-align:center;">
                    <a href="/map"><img src="/images/mapa-uklidu.jpg" class="img-responsive" style="position: relative; top: -17px; " alt="Mapa úklidů" title="Mapa úklidů"></a>
                    <!-- <div class="flex-video" style="margin: 0 auto; text-align:center;">
                        <iframe allowfullscreen="" src="//www.youtube.com/embed/7LFiUC156GE?feature=player_detailpage&html5=1" frameborder="0"></iframe>
                    </div>
                    -->
                </div>
            </div>
            <!--
            <div class="col-sm-6 col-md-3 hidden-xs">
                <div class="flex-video thumbnail" style="margin: 0 auto; text-align:center;">
                    <a href="http://www.ekofilm.cz" target="_blank"><img src="http://res.cloudinary.com/uklidmecesko/image/upload/v1445965323/ekofilm2015.jpg"  class="img-responsive" style="position: relative; top: -17px; " alt="EKOFILM 2015" title="EKOFILM 2015" /></a>
                    <iframe allowfullscreen="" src="//www.youtube.com/embed/ep_VQ1cof8M?feature=player_detailpage&html5=1" frameborder="0"></iframe>
                </div>
            </div>
            -->
        </div>
    </div>


    
