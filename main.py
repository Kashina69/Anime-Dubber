import re
import subprocess


def extract_subtitles(video_file, output_file="subtitles.srt"):
  """
  Extracts subtitles from an MKV video file using ffmpeg.

  Args:
      video_file (str): Path to the MKV video file.
      output_file (str, optional): Path to save the extracted subtitles in SRT format. Defaults to "subtitles.srt".
  """
  # Build the ffmpeg command
  command = ["ffmpeg", "-i", video_file, "-map", "0:s", output_file]

  # Execute the command and capture output (optional for error handling)
  subprocess.run(command, check=True)

  print(f"Subtitles extracted to: {output_file}")

# Example usage
video_file = "E:\Software\Programms\Project\Anime Dubber\\1098.mkv"
extract_subtitles(video_file)


def clean_srt_file(filename):
  """
  Opens an SRT file, cleans each line by removing HTML tags,
  and returns a list of cleaned lines.
  """
  cleaned_lines = []
  pattern = r"<.*?>|\\{.*?\\}"  # Regex to remove HTML and curly braces

  with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
      cleaned_line = re.sub(pattern, "", line, flags=re.DOTALL)
      cleaned_lines.append(cleaned_line)

  return cleaned_lines

filename = "subtitles.srt"
cleaned_text = clean_srt_file(filename)
for line in cleaned_text:
  with open("new subtitles.srt","a", encoding='utf-8') as file:
    file.write(line)


def read_file(filename):
  print


read_file("new subtitles.srt")


