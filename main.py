from pydub import AudioSegment

def remove_part_from_mp3(input_file, start_time, end_time, output_file):
    audio = AudioSegment.from_mp3(input_file)

    print(f"Duration of the audio file: {audio.duration_seconds} seconds.")
       

    if start_time < 0 or end_time > len(audio):
        print("Invalid start or end time.")
        return
    

    before_part = audio[:start_time]
    after_part = audio[end_time:]
    

    final_audio = before_part + after_part #merging
    

    final_audio.export(output_file, format="mp3")
    print(f"File exported as: {output_file}")

input_mp3 = input("Enter the MP3 file name: ")
start = int(input("Enter the start of the section to remove (in milliseconds): "))
end = int(input("Enter the end of the section to remove (in milliseconds): "))
output_mp3 = "output.mp3"

remove_part_from_mp3(input_mp3, start, end, output_mp3)
