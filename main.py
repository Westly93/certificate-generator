import cv2


font_face = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 3.0
font_thickness = 2
line_spacing = 200


list_names = ["weston Mufudza", "Tafara Mukute",
              "Nicholas Chaibva", "Emmanuel Jeche"]
course_list = ["Inroduction to programming", "Introduction to Web development",
               "How to become a fullstack Developer", "Advanced Programming with Python"]

for index, name in enumerate(list_names):
    # Split the course name into multiple lines based on the maximum width
    certificate = cv2.imread("./template/template.png")
    max_width = int(certificate.shape[1] * 0.8)
    words = course_list[index].split()
    lines = []
    current_line = ''
    for word in words:
        text = current_line + ' ' + word if current_line else word
        (text_width, _) = cv2.getTextSize(
            text, font_face, font_scale, font_thickness)[0]

        if text_width <= max_width:
            current_line = text
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)  # Add the last line

    # Calculate the starting position for the text
    text_x = int(certificate.shape[1] * 0.1)  # Adjust the x-position as needed
    text_y = int(certificate.shape[0] * 0.6)  # Adjust the y-position as needed

    # Write the student name on the certificate
    cv2.putText(certificate, name, (400, 1833),
                font_face, 4, (0, 0, 0), font_thickness)

    # Write the course name on the certificate, each line on a new line
    for i, line in enumerate(lines):
        line_y = 2200 + (i + 1) * line_spacing
        cv2.putText(certificate, line, (text_x+(i*200), line_y), font_face,
                    font_scale, (0, 0, 0), font_thickness)

    # Display or save the resulting certificate image
    cv2.imwrite(f'certificates/{name}.png', certificate)
    print(f"Processing Certificate {index + 1} of {len(list_names)}")
