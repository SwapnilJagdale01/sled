
  // Initialize Firebase
//   var config = {
//     apiKey: "AIzaSyBsMQlGknjN27naDZFz5SBgWY2XR7w-n0U",
//     authDomain: "traineaux-fdf39.firebaseapp.com",
//     databaseURL: "https://traineaux-fdf39.firebaseio.com",
//     projectId: "traineaux-fdf39",
//     storageBucket: "traineaux-fdf39.appspot.com",
//     messagingSenderId: "857150252986"
//   };
  
// firebase.initializeApp(config);

function operations(newPostKey) {


// var newPostKey = firebase.database().ref().child("Session").push().key;
// var directionId = {};
// directionId["current"] = newPostKey;
// firebase.database().ref().child("direction").update(directionId);
// var state = {};
// state["currentState"] = false;
// var stateRef = firebase.database().ref("direction");
// stateRef.update(state);

var SleighTracingRef1 = firebase.database().ref('Session/'+newPostKey+'/Sleigh/Tracing/1');
SleighTracingRef1.on("child_added", function(SleighTracingSanp1){
  $( "#btnSheet" ).trigger( "click" );
  console.log("click");
});

var SleighTracingRef0 = firebase.database().ref('Session/'+newPostKey+'/Sleigh/Tracing/0');
SleighTracingRef0.on("child_added", function(SleighTracingSanp0){
  $( "#ncBtnSheet" ).trigger( "click" );
});

var SleighCuttingRef1 = firebase.database().ref('Session/'+newPostKey+'/Sleigh/Cutting/1');
SleighCuttingRef1.on("child_added", function(SleighCuttingSanp1){
  $( "#btnCut" ).trigger( "click" );
});

var SleighCuttingRef0 = firebase.database().ref('Session/'+newPostKey+'/Sleigh/Cutting/0');
SleighCuttingRef0.on("child_added", function(SleighCuttingSanp0){
  $( "#ncBtnCut" ).trigger( "click" );
});

var SleighFoldingRef1 = firebase.database().ref('Session/'+newPostKey+'/Sleigh/Folding/1');
SleighFoldingRef1.on("child_added", function(SleighFoldingSanp1){
  $( "#btnFold" ).trigger( "click" );
});

var SleighFoldingRef0 = firebase.database().ref('Session/'+newPostKey+'/Sleigh/Folding/0');
SleighFoldingRef0.on("child_added", function(SleighFoldingSanp0){
  $( "#ncBtnFold" ).trigger( "click" );
});

var SleighPunchingRef1 = firebase.database().ref('Session/'+newPostKey+'/Sleigh/Punching/1');
SleighPunchingRef1.on("child_added", function(SleighPunchingSanp1){
  $( "#btnSleighPunching" ).trigger( "click" );
});

var SleighPunchingRef0 = firebase.database().ref('Session/'+newPostKey+'/Sleigh/Punching/0');
SleighPunchingRef0.on("child_added", function(SleighPunchingSanp0){
  $( "#ncBtnSleighPunching" ).trigger( "click" );
});

var SleighAssemblyRef1 = firebase.database().ref('Session/'+newPostKey+'/Sleigh/Assembly/1');
SleighAssemblyRef1.on("child_added", function(SleighAssemblySanp1){
  $( "#btnAssembly" ).trigger( "click" );
});

var SleighAssemblyRef0 = firebase.database().ref('Session/'+newPostKey+'/Sleigh/Assembly/0');
SleighAssemblyRef0.on("child_added", function(SleighAssemblySanp0){
  $( "#ncBtnAssembly" ).trigger( "click" );
});

var SkiFoldingRef1 = firebase.database().ref('Session/'+newPostKey+'/Ski/Folding/1');
SkiFoldingRef1.on("child_added", function(SkiFoldingSanp1){
  $( "#btnSkiFolding" ).trigger( "click" );
});

var SkiFoldingRef0 = firebase.database().ref('Session/'+newPostKey+'/Ski/Folding/0');
SkiFoldingRef0.on("child_added", function(SkiFoldingSanp0){
  $( "#ncBtnSkiFolding" ).trigger( "click" );
});

var SkiPunchingRef1 = firebase.database().ref('Session/'+newPostKey+'/Ski/Punching/1');
SkiPunchingRef1.on("child_added", function(SkiPunchingSanp1){
  $( "#btnSkiPunching" ).trigger( "click" );
});

var SkiPunchingRef0 = firebase.database().ref('Session/'+newPostKey+'/Ski/Punching/0');
SkiPunchingRef0.on("child_added", function(SkiPunchingSanp0){
  $( "#ncBtnSkiPunching" ).trigger( "click" );
});

var SeatFoldingRef1 = firebase.database().ref('Session/'+newPostKey+'/Seat/Folding/1');
SeatFoldingRef1.on("child_added", function(SeatFoldingSanp1){
  $( "#btnSeatFolding" ).trigger( "click" );
});

var SeatFoldingRef0 = firebase.database().ref('Session/'+newPostKey+'/Seat/Folding/0');
SeatFoldingRef0.on("child_added", function(SeatFoldingSanp0){
  $( "#ncBtnSeatFolding" ).trigger( "click" );
});




}


// $( "#startTimer" ).click(function() {
//   var state = {};
//   state["currentState"] = true;
//   var stateRef = firebase.database().ref("direction");
//   stateRef.update(state);
//   start_job();
//   incrementByTenMilliseconds.start();
// });

// $( "#pauseTimer" ).click(function() {
//   var state = {};
//   state["currentState"] = false;
//   var stateRef = firebase.database().ref("direction");
//   stateRef.update(state);
//   resume_job();
//   incrementByTenMilliseconds.resume();
// });

// $( "#stopTimer" ).click(function() {
//   var state = {};
//   state["currentState"] = false;
//   var stateRef = firebase.database().ref("direction");
//   stateRef.update(state);
//   stop_job();
//   incrementByTenMilliseconds.stop();
//   //window.location.reload();
// });

//                 function start_job() {
//                     var url = "/start_job/";
//                     var text = "";
//                     $.ajax({
//                         type: 'POST',
//                         url: url,
//                         data: {
//                             'text': text,
//                             csrfmiddlewaretoken: String(document.cookie.split('csrftoken')).split("=")[1]
//                         },
//                         success: function (data) {
//                             console.log(JSON.stringify(data));
//                         },
//                         error: function (xhr, msg, err) {
//                             $("#loginError").text(xhr.responseJSON.error);
//                         }

//                     });
//                 }

//                 function resume_job() {
//                     var url = "/resume_job/";
//                     var text = "";
//                     $.ajax({
//                         type: 'POST',
//                         url: url,
//                         data: {
//                             'text': text,
//                             csrfmiddlewaretoken: String(document.cookie.split('csrftoken')).split("=")[1]
//                         },
//                         success: function (data) {
//                             console.log(JSON.stringify(data));
//                         },
//                         error: function (xhr, msg, err) {
//                             $("#loginError").text(xhr.responseJSON.error);
//                         }

//                     });
//                 }

//                 function stop_job() {
//                     var url = "/stop_job/";
//                     var text = "";
//                     $.ajax({
//                         type: 'POST',
//                         url: url,
//                         data: {
//                             'text': text,
//                             csrfmiddlewaretoken: String(document.cookie.split('csrftoken')).split("=")[1]
//                         },
//                         success: function (data) {
//                             console.log(JSON.stringify(data));
//                         },
//                         error: function (xhr, msg, err) {
//                             $("#loginError").text(xhr.responseJSON.error);
//                         }

//                     });
//                 }