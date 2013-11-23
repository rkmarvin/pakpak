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
    }
    audio_setup();
};

