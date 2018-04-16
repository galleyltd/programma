### Docker way

1. Add bot token in bot.py

2. If you want to have fast build, download manually `stanford-corenlp-full-2018-02-27.zip` and 
place it in the root of the project.

Otherwise - uncomment line in `Dockerfile-corenlp` ```# ADD http://nlp.stanford.edu/software/stanford-corenlp-full-2018-02-27.zip .```

3. Run docker by doing:

`docker-compose up --build`

4. Send messages in the chat with ProGramma bot

5. Open `localhost:8080/stats` for advanced statistics