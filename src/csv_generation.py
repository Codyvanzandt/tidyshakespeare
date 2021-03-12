import csv

def generate_csv(play, file_path):
    with open(file_path, "w") as output_file:
        fieldnames = ["title", "act", "scene", "line", "kind", "who", "text"]
        writer = csv.DictWriter(output_file, fieldnames=fieldnames, delimiter="\t", quotechar="|")
        writer.writeheader()
        for act in play.acts:
            for scene in act.scenes:
                for line in scene.lines:
                    writer.writerow({
                        "title" : play.title,
                        "act" : act.number,
                        "scene" : scene.number,
                        "line" : line.number,
                        "kind" : line.kind,
                        "who" : line.who,
                        "text" : line.text
                    })