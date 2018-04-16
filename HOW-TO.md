### Docker way

1. Add bot token in bot.py

2. Run docker by doing:

If you want to have fast build, download manually `stanford-corenlp-full-2018-02-27.zip` and 
place it in the root of the project.

Otherwise - uncomment line in `Dockerfile-corenlp` ```# ADD http://nlp.stanford.edu/software/stanford-corenlp-full-2018-02-27.zip .```

`docker-compose up --build`

3. Send messages in the chat with ProGramma bot

4. Open `localhost:8080/stats` for advanced statistics