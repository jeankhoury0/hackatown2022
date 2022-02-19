# Take out the trash
## Get reminded to take out the trash


### Inspiration
We always always forget to take out the trash! I wake up, hear the disposal truck go by my house and this make me mad! Why can't I be reminded to take out the trash the day before! If this is also a problem that you are facing, then you are not alone! Last year, the city of Montreal received 109 000 information requests for the different garbage collection services open data. This account to about 25 hours of work a day responding to questions that could be easily automated.

### What it does
Take out the trash is an SMS notification platform that will remind you the day before to take out the trash or other type of garbage (Household waste collection, Recycling collection, Collection of construction, renovation and demolition debris and bulky items and irregular collections ...) We want this service to be available to the public but also to be integrated to the 311 call center so that an agent can subscribe anyone calling so they don't call again! We choose SMS over notification so that anybody will be able to receive the alert even if they don't have a smartphone or if they are from low income households (you don't need that much technology to receive an sms!)

### How we built it
We where thrilled to learn that Twilio was a part of the challenge! We used Python flask to build a form that subscribe the user to notifications. The forms address is validated with google place API. When validating the form, the user data is saved to a DB (mongoDB) and a task is added to the task queue (Celery). The user then receive the day before that the trash needs to be taken out! This data is queried from the various trash collections APIs available via the open data portal. Finally we hosted the website on Heroku but plan to move to a better storage solution if time permits.

### Challenges we ran into
- SOO MANY APIs that we needed to learn in such a short time frame (We all have headaches!). Ever heard of GeoJson? Its an amazing technology but its soo complicated to get working.
- First time using python Flask to build a website. Only one member of the team has web dev experience but never in Flask.
- We learned too late that Twilio API wont send SMS even with the MLH promo code. ** For this reason the phone numbers** working are only the ones of our teams. Don't hesitate to contact us if you want us to put your phone number in the database so that you can test it out yourself.

### Accomplishments that we're proud of
- We learned a new framework in such a small amount of time
- We where able to connect different services
- The app is quite good for only 24ish hours of work
- From something that was planned Friday evening we are impressed that we had the time to integrate most of the features !

### What we learned
- Always always test a service before planning your app around it
- Never publish secrets keys on GitHub public even if you want to go fast (we received 10 alert emails)
- Don't tell yourself its not possible just do it :)
