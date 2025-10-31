function b() {
Email.send({
    Host : "smtp.stand-up.a2hosted.com",
    Username : "standup3@smtp.stand-up.a2hosted.com",
    Password : "7[Gas4BxjI6&",
    To : 'mmistry169@gmail.com',
    From : "standup3@smtp.stand-up.a2hosted.com",
    Subject : "This is the subject",
    Body : "And this is the body"
}).then(
  message => alert(message)
);
}