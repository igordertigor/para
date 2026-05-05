# para

I'm organizing folders on my computer using the PARA system:

- `~/projects`: Contains directories that relate to time limited efforts with a clear start and end criterion. Directories in the projects folder should be short-lived. As such, I regularly check if projects are finished or abandoned. I try to keep my projects directory small.
- `~/areas`: Are topics that I regularly revisit with no actual time limit. I try to keep the areas directory small and rather spawn projects for most of the actual work.
- `~/reference`: This is the place for documents that I don't typically change but that I refer to regularly. Maybe a list of tax numbers or recovery codes for some account. Maybe a cheat sheet for a tool I'm trying to learn.
- `~/archive`: when I'm done with a project, I move it to the archive. Here, I have all past projects organized by end date.

There is no secret magic about this system. The key point is that it's easy to stick with it and that I never have to think where to save an attachment. Receiving a tax relevant receipt by email? Store it in `~/projects/tax-2026/receipts/`. All the receipts for my vacation rentals? In `~/projects/italy-in-summer/`.

This repository contains a few commands to keep the different directories structured. At the moment, that means in particular the interplay between `~/projects` and `~/archive`:

- `para init <description>` creates a new project directory at `~/projects/<description>` and adds a `STATUS.md` file to facilitate easy status tracking.
- `para archive <directory>` archives the respective project directory and sorts it into the correct year subdirectory.

## Planned features

- Status shows "next" action if available
- Linking areas and projects
- Semantic search in archive
