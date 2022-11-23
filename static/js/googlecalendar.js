document.addEventListener('DOMContentLoaded', function() {
	let calendarEl = document.getElementById('calendar');

	let calendar = new FullCalendar.Calendar(calendarEl, {

		headerToolbar: {
			left: 'prev,next today',
			center: 'title',
			right: 'dayGridMonth,listYear'
		},

		displayEventTime: false,

		//googleカレンダーAPIキー
		googleCalendarApiKey: apiconfig.apikey, 
		//カレンダーのID
		events: apiconfig.ID, 

		eventClick: function(arg) {
			window.open(arg.event.url, 'google-calendar-event', 'width=700,height=600');
			arg.jsEvent.preventDefault() // don't navigate in main tab
		},

		loading: function(bool) {
			document.getElementById('loading').style.display =
				bool ? 'block' : 'none';
		}

	});

	calendar.render();
});

