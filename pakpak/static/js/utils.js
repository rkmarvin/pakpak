function init()
{
    var i=0;
    var nextSong= "";
    var audioPlayer = document.getElementById('audio');
    function audio_setup() {
        document.getElementById('audio').addEventListener('ended', function(){
            i++
            nextSong = $('#song_' + i).attr('href');
            audioPlayer.src = nextSong;
            audioPlayer.load();
            audioPlayer.play();
            if(i == $('#play_list').attr('count'))
            {
                i = 0;
            }
        }, false);
    };

    $('.song').on('click', function(e){
        var src = $(e.target).attr('href');
        var audio = $('<audio controls="controls" align="" autoload/>').attr('src', src)
        
        $('#' + $(e.targer).id).append(audio);

        console.log(src);
        console.log(audio);
        console.log('done');
    });
    audio_setup();
};

