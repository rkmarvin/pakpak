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
        $('.song').css('background', 'white') 
        $(e.target).css('background', 'red') 

        nextSong = $(e.target).attr('href');
        audioPlayer.src = nextSong;
        audioPlayer.load();
        audioPlayer.play();
    });
    audio_setup();
};

