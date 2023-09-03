# YT NOTE
#### Video Demo:  <URL https://www.youtube.com/watch?v=i0Sxj4pztXk>
#### Description:
This WebApplication can be use to create annotations about youtube videos.

The annotations will be shown in a block that will contain informations like: 
Title, the video thumbmail and description.

The annotation can be modifyed, deleted or marked as well.

#### Way to use:
The index page contain a form that have the fields title, url and descriptions.

In the field title you can insert a text that will be show in your annotation, the 
text can be none or different to the youtube video title.

In the url field, you can insert a youtube video url. For this application the 
url needs to have only one signal '='. 
Example: "https://www.youtube.com/watch?v=" + "video id"

The url cannot be a list of youtube video.

In the description field, you insert a brief text to describe your annotation

#### The annotation page

This page will show all of your annotation that is in the sqlite database, it 
will be in a box that contains the title, thumbmail, and description as well as
buttons to delete, edit, and mark the box.

#### How to edit the box:

When in the annotation page, you can click in the edit button and it will redirect
to the edit page.

The edit page will be simillar to the index page. It will contain the same fields
but with the value inserted that you can change.

#### Hot to delete a box:

In the annotations page, just click on the delete button and it will remove the
data by id in the database, and also delete from the page.

#### Mark button:

The mark button will change the color of the box to orange. It can be used to mark
about something. Ideas: Mark after watched, Marked as good.


