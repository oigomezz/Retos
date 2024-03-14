import re


def handles_detector(text):
    handles = {}

    handles["user"] = re.findall(r"@(\w{2,15})", text)
    handles["hashtag"] = re.findall(r"#[^ !@$^#&,.?():%<>{}\[\]|\"+]+", text)
    handles["url"] = re.findall(
        r"((https?://(www\.)?)|www\.)[\w#+\=]{2,256}\.[a-zA-Z]{2,7}[\w\/?=&.+-]*", text
    )

    return handles


print(
    handles_detector(
        "En esta actividad de @mouredev, resolvemos #retos de #programacion desde https://retosdeprogramacion.com/semanales2022, que @braismoure aloja en www.github.com"
    )
)
