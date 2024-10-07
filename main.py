import writer
import reader
import library

babel = library.Library()
satan = writer.Writer()
job = reader.Reader()

satan.write_book()
babel.shelf.append(satan.current_book)

job.check_book(satan.current_book)

print(job.highscore)
