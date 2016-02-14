function playSomeSound (genre) {
	SC.get('/tracks', {
		genres: genre,
		bpm: {
			from: 100
		}
	}, function(tracks) {
		var random = Math.floor(Math.random() * 49):
		Sc.oEmbed(tracks[random].uri, { auto_play: true }, document.getElementById('target'));
	});
}

window.onload = function() {
	SC.initialize( {
		client_id = '03f5fa9ff584245dfd36e371ea7bee3c'
	});
}