# Remote Forge<!-- omit from toc -->

Welcome to Remote Forge, my creation and your gateway to the world of remote work opportunities. This platform is a result of my vision to connect talented professionals with the freedom and flexibility that remote jobs offer. Remote Forge stands as a testament to my belief that great work isn't confined to an office—it can happen anywhere.

![Remote Forge](./docs/remote-forge-presentation.webp)

![GitHub contributors](https://img.shields.io/github/issues/patrickhladun/remote-forge?style=flat) ![GitHub last commit (branch)](https://img.shields.io/github/last-commit/patrickhladun/remote-forge/main?style=flat) ![GitHub language count](https://img.shields.io/github/languages/count/patrickhladun/remote-forge?style=flat) ![GitHub top language](https://img.shields.io/github/languages/top/patrickhladun/remote-forge?style=flat)

## Table of Contents<!-- omit from toc -->

- [Project Scope and Objectives](#project-scope-and-objectives)
  - [Website Objectives](#website-objectives)
  - [Key components of the website include](#key-components-of-the-website-include)
- [User Experience](#user-experience)
  - [Audience Persona: Talent - Siobhan O'Neill](#audience-persona-talent---siobhan-oneill)
  - [Audience Persona: Employer - Eoin McCarthy](#audience-persona-employer---eoin-mccarthy)
- [User Goals](#user-goals)
  - [Talent - Siobhan O'Neill's Goals:](#talent---siobhan-oneills-goals)
  - [Employer - Eoin McCarthy's Goals:](#employer---eoin-mccarthys-goals)
- [Agile Methodology in Project Development](#agile-methodology-in-project-development)
  - [Epics](#epics)
- [Five Planes of UX](#five-planes-of-ux)
- [Wireframes](#wireframes)
- [Mockups](#mockups)
- [Database Design](#database-design)
- [Colours Scheme](#colours-scheme)
- [Fonts](#fonts)
- [Logo](#logo)
- [Images](#images)
  - [Profile Images](#profile-images)
- [Icons](#icons)
- [Pages and Features](#pages-and-features)
  - [Front End Pages](#front-end-pages)
  - [User and Content Management Pages](#user-and-content-management-pages)
    - [Profile Management for Talent and Employers](#profile-management-for-talent-and-employers)
    - [Account Management](#account-management)
  - [Job Management for Employers](#job-management-for-employers)
  - [Django Administration](#django-administration)
- [Technology used](#technology-used)
  - [Languages and Libraries](#languages-and-libraries)
  - [Version Control and Collaboration](#version-control-and-collaboration)
  - [Tooling](#tooling)
  - [Design Tools](#design-tools)
  - [Testing and Validation](#testing-and-validation)
  - [Other](#other)
- [Development and Deployment](#development-and-deployment)
  - [Cloning the project](#cloning-the-project)
  - [Environment Settings](#environment-settings)
    - [Development](#development)
    - [Staging and Production](#staging-and-production)
    - [Environment Variables Template](#environment-variables-template)
  - [Local Development](#local-development)
  - [Deployment on Heroku](#deployment-on-heroku)
  - [Load Example Content](#load-example-content)
    - [Load Fixtures Locally](#load-fixtures-locally)
    - [Load Example Content for Staging Site](#load-example-content-for-staging-site)
- [Manual testing](#manual-testing)
  - [Website Header and Navigation](#website-header-and-navigation)
  - [Responsive Design Tests](#responsive-design-tests)
  - [Functionality tests](#functionality-tests)
    - [Admin Pages](#admin-pages)
  - [Google PageSpeed Insights Tests](#google-pagespeed-insights-tests)
  - [HTML Validation and Accessibility Testing](#html-validation-and-accessibility-testing)
  - [Testing User Pages](#testing-user-pages)
  - [CSS Validation](#css-validation)
- [Automated testing with Pytest](#automated-testing-with-pytest)
  - [Running Tests](#running-tests)
- [Issues](#issues)
  - [User Stories](#user-stories)
  - [Bugs](#bugs)
- [Credits](#credits)
- [Acknowledgments](#acknowledgments)

## Project Scope and Objectives

[Back to Top](#table-of-contents)

The core objective of Remote Forge is to develop a comprehensive Full-Stack MVP that serves as a robust platform for remote work opportunities. This project is designed with the specific goal of connecting talented professionals seeking remote work with employers looking to hire for remote roles. By focusing solely on 100% remote opportunities, Remote Forge aims to become a specialized hub for those passionate about flexible working arrangements, thereby addressing the growing demand for remote work in various industries.

### Website Objectives

[Back to Top](#table-of-contents)

- Create a dynamic environment where employers can easily find and connect with skilled professionals ready to embrace remote work opportunities.
- Provide an intuitive platform for job seekers to discover job listings that match their skills and preferences, enabling straightforward applications to their chosen roles.
- Offer employers a user-friendly interface for creating, managing, and tracking job postings, ensuring a smooth recruitment process.
- Allow talents to showcase their skills, experience, and work preferences through detailed profiles, increasing their visibility to potential employers.

### Key components of the website include

[Back to Top](#table-of-contents)

- **User Authentication System:** A secure login and registration process for two distinct user types: Employers and Talents, with role-specific access to features and functionalities.
- **Dynamic Job Board:** A central repository for job listings, offering search and filter capabilities to help Talent users find suitable job opportunities.
- **Employer and Talent Profiles:** Dedicated sections for users to create and manage their professional profiles, including the ability to post comprehensive job descriptions for Employers and detailed resumes for Talents.
- **CRUD Operations for Job Listings:** A set of functionalities that allows Employers to create, read, update, and delete job postings as their hiring needs evolve.
- **Content Pages:** Static pages such as Home, About, and Contact, providing users with information about Remote Forge, its mission, and how to get in touch.
- **Application and Applicant Management (optional):** For Employers, an optional feature to track and manage applications received for their job listings; for Talents, the ability to apply directly to jobs or through external links provided by Employers.

## User Experience

[Back to Top](#table-of-contents)

### Audience Persona: Talent - Siobhan O'Neill

[Back to Top](#table-of-contents)

<details><summary>Demographics</summary>

- Location: Cork, Ireland
- Age: 29
- Education: Bachelor's Degree in Digital Marketing
- Occupation: Freelance Digital Marketer
- Income Level: Mid-level, primarily project-based earnings

</details>

<details><summary>Psychographics</summary>

Siobhan values flexibility and autonomy over her work schedule and environment. She is driven by opportunities to grow her skill set and seeks roles that challenge her creatively. Sustainability and work-life balance are important to her, influencing her job selection process.

</details>

<details><summary>Behavioral Traits</summary>

Siobhan actively seeks out remote work opportunities that allow her to blend her professional ambitions with her personal lifestyle. She prefers long-term contracts or permanent remote positions that offer stability. Siobhan is proactive in networking and continuously learning new skills relevant to her field.

</details>

<details><summary>Online Habits</summary>

Frequently uses LinkedIn and Twitter for networking and industry news. Siobhan relies on specialized job boards focused on remote work and digital marketing forums to find new opportunities. She attends webinars and online courses to enhance her skills and is active in several online communities related to digital marketing and remote work.

</details>

<details><summary>How Remote Forge Meets Siobhan's Needs</summary>

Remote Forge provides Siobhan with access to a curated list of remote job opportunities in her field, allowing her to apply her skills in roles that value creativity and strategic thinking. The platform's focus on remote roles aligns with her desire for work-life balance and professional growth. With features for networking and profile visibility, Siobhan can showcase her portfolio and connect with potential employers in Ireland and beyond, who are looking for her unique skill set.

</details>

### Audience Persona: Employer - Eoin McCarthy

[Back to Top](#table-of-contents)

<details><summary>Demographics:</summary>

- Location: Dublin, Ireland
- Age: 35
- Position: HR Manager
- Industry: Technology Startup
- Company Size: 50-200 employees

</details>

<details><summary>Psychographics</summary>

Eoin values innovation and agility within his company's workforce. He believes in building a diverse team that brings a wide range of perspectives and skills. Eoin is focused on recruiting top talent that aligns with the startup's dynamic and innovative culture, emphasizing the importance of adaptability and continuous learning.

</details>

<details><summary>Behavioral Traits</summary>

Actively seeks platforms that can streamline the recruitment process, making it easier to post jobs and manage applications. Eoin prioritizes efficiency and quality in recruitment, looking for tools that can help him find the best match for open positions quickly. He values clear communication and transparency with potential candidates.

</details>

<details><summary>Online Habits</summary>

Uses LinkedIn for professional networking and industry insights. Eoin frequently visits tech and startup-focused job boards to scout for talent and to stay updated on hiring trends. He participates in online forums and webinars on talent acquisition strategies and HR technology to enhance his recruitment methods.

</details>

<details><summary>How Remote Forge Meets Eoin's Needs</summary>

Remote Forge offers Eoin a specialized platform to reach a broad pool of candidates seeking remote opportunities, particularly in the tech sector. The site's emphasis on remote roles aligns with the startup's flexible and forward-thinking employment policies. Remote Forge's streamlined job posting and applicant management features allow Eoin to efficiently sort through candidates, focusing on those who meet the specific requirements of the role and fit the company culture. The platform also enables Eoin to showcase his company's mission, culture, and values through a detailed employer profile, attracting candidates who are not just skilled but also a good cultural fit for the startup.

</details>

## User Goals

[Back to Top](#table-of-contents)

### Talent - Siobhan O'Neill's Goals:

- Find Relevant Job Listings: Siobhan aims to find remote job opportunities that match her skills in digital marketing, allowing her to work flexibly and maintain a work-life balance.
- Network with Potential Employers: She seeks to connect with companies and HR managers like Eoin, who value creativity and strategic thinking, and are open to remote work arrangements.
- Showcase Her Skills and Experience: Siobhan wants to effectively present her portfolio and professional achievements on her profile to attract the right employers.
- Stay Informed and Up-to-Date: She aims to keep abreast of the latest trends in digital marketing and remote work opportunities through networking and continuous learning.
- Secure Stable Employment: Ultimately, Siobhan's goal is to secure a long-term contract or permanent position that aligns with her career aspirations and personal values.

### Employer - Eoin McCarthy's Goals:

- Attract Top Talent: Eoin is focused on attracting skilled professionals like Siobhan, who can bring innovation and creativity to his tech startup.
- Simplify the Recruitment Process: He aims to streamline the job posting and application management process to efficiently find the best candidates.
- Enhance Company Visibility: Eoin wants to effectively communicate his startup's culture, mission, and values through the employer profile to attract candidates who are not just skilled but also a good cultural fit.
- Build a Diverse and Dynamic Team: He seeks to recruit from a diverse pool of candidates to foster innovation and agility within the team.
- Ensure Quality and Fit: Eoin's goal is to use platforms like Remote Forge to not only find candidates with the right skills but also to ensure they align with the startup's dynamic and innovative work environment.

## Agile Methodology in Project Development

[Back to Top](#table-of-contents)

In developing Remote Forge, I've embraced agile methodology to ensure flexibility, continuous improvement, and responsiveness to user feedback. This approach allows me to quickly adapt to changes and prioritize tasks effectively, focusing on delivering value at every stage of development.

To manage the project efficiently, I utilize GitHub Issues and Projects alongside a Kanban board. This setup is crucial for organizing my workflow and keeping track of progress. Additionally, I use GitHub Milestones to structure Sprints, helping me stay on track with deadlines and deliverables.

<details><summary>Sprints using Milestones</summary>

![Sprints](./docs/agile-sprints.webp)

</details><br>

Kanban Board: My Kanban board features columns for Backlog, In Progress, Paused/on Hold, Verification/Testing and Done, offering a clear visual guide to the project's status and allowing me to efficiently manage tasks from conception to completion.

[Kanban View](https://github.com/users/patrickhladun/projects/5/views/1)

<details><summary>Kanban View</summary>

![Kanban View](./docs/agile-kanban.webp)

</details><br>

I also use GitHub's Table view to organize and visualize tasks, providing a clear and structured overview of the project's progress and priorities.

[Table View](<[./docs/](https://github.com/users/patrickhladun/projects/5/views/3)>)

<details><summary>Table View</summary>

![Table View](./docs/agile-table.webp)

</details><br>

Epics and User Stories: I break down the development into Epics and User Stories, making the project manageable and ensuring each feature closely aligns with user needs.

[Github Remote Forge Project](https://github.com/users/patrickhladun/projects/5)

### Epics

- [Epic 1: Project setup and planning](https://github.com/patrickhladun/remote-forge/issues/1)
- [Epic 2: Design and assets development](https://github.com/patrickhladun/remote-forge/issues/19)
- [Epic 3: Frontend and backend development for 'Remote Forge' MVP](https://github.com/patrickhladun/remote-forge/issues/3)
- [Epic 4: Testing deployment and documentation](https://github.com/patrickhladun/remote-forge/issues/9)

By adopting agile methodology and utilizing GitHub's robust project management tools, I navigate the development of Remote Forge with agility, keeping the project aligned with its core mission of connecting the remote work community.

## Five Planes of UX

[Back to Top](#table-of-contents)

The 5 Planes of User Experience (UX) provide a framework for understanding the layers involved in creating a user-centered design. This model, conceptualized by Jesse James Garrett in his book "The Elements of User Experience," outlines how UX designers can move from abstract to concrete in the process of designing digital products. Here’s how these planes can be applied to the development of Remote Forge:

1. Strategy Plane

- User Needs: For Remote Forge, understanding the needs of two primary user groups—Talents seeking remote work and Employers looking to hire remote talent—is crucial. Talents desire easy access to job listings, straightforward application processes, and the ability to showcase their skills. Employers need to efficiently post jobs, manage applications, and find suitable candidates.
- Site Objectives: The main objective is to create a platform that facilitates the connection between remote job seekers and employers, offering a streamlined experience for both parties to find and fill remote work opportunities.

2. Scope Plane

- Functional Specifications: Key functionalities include user registration and authentication, job listing creation and management by Employers, profile creation and job application for Talents, and search and filter capabilities for job listings.
- Content Requirements: Content such as job descriptions, company profiles, talent bios, educational articles on remote work, and FAQs will be developed to engage users and provide valuable resources.

3. Structure Plane

- Interaction Design: The interaction design will focus on how users interact with Remote Forge, including navigating the site, filling out forms, and managing profiles or job listings. The goal is to ensure intuitive, seamless interactions that guide users through their journey on the platform.
- Information Architecture: The information architecture will organize and structure content and functionalities in a way that makes sense to the users, ensuring they can find information and perform tasks with ease.

4. Skeleton Plane

- Interface Design: This involves designing the layout of web pages and user interfaces for Remote Forge, ensuring that elements such as buttons, forms, and navigation menus are laid out in a user-friendly manner. Navigation Design: The navigation system will be designed to allow users to easily move between different parts of the site, with clear labels and logical grouping of site sections.
- Information Design: The presentation of information, such as job listings and profiles, will be structured for clarity and ease of understanding, making use of headings, lists, and visual cues to guide the user’s eye.

5. Surface Plane

- Visual Design: The final layer involves choosing colors, typography, and imagery that align with the Remote Forge brand and appeal to the target audience. The visual design will enhance the usability of the platform while making it aesthetically pleasing, aiming to create a positive first impression and engaging user experience.

## Wireframes

[Back to Top](#table-of-contents)

For the initial design phase of Remote Forge, I used Figma to create the wireframes. Figma's versatility makes it ideal for developing both wireframes and mockups in the same environment. In this section, I'll showcase the wireframes that laid the groundwork for all key pages of the platform.

<details><summary>Wireframe Home</summary>

![Home Page](./docs/wireframe-home.webp)

</details>

<details><summary>Wireframe About</summary>

![About Page](./docs/wireframe-about.webp)

</details>

<details><summary>Wireframe Contact</summary>

![Contact Page](./docs/wireframe-contact.webp)

</details>

<details><summary>Wireframe Feed Pages</summary>

![Feed Pages](./docs/wireframe-feed-pages.webp)

</details>

<details><summary>Wireframe Single Job</summary>

![Single Job](./docs/wireframe-single-job.webp)

</details>

<details><summary>Wireframe Talent Profile</summary>

![Talent Profile](./docs/wireframe-talent-profile.webp)

</details>

<details><summary>Wireframe Employer Profile</summary>

![Employer Profile](./docs/wireframe-employer-profile.webp)

</details>

<details><summary>Wireframe Account Forms</summary>

![Account Forms](./docs/wireframe-account-forms.webp)

</details>

## Mockups

[Back to Top](#table-of-contents)

Building on the foundational wireframes, I progressed to designing detailed mockups for Remote Forge using Figma. These mockups are refined visual representations of the website, incorporating color schemes, typography, and imagery to bring the initial wireframe structures to life.

<details><summary>Mockup Home Page</summary>

![Home Page](./docs/mockup-home.webp)

</details>

<details><summary>Mockup About Page</summary>

![About Page](./docs/mockup-about.webp)

</details>

<details><summary>Mockup Contact Page</summary>

![Contact Page](./docs/mockup-contact.webp)

</details>

<details><summary>Mockup Job Feed Page</summary>

![Job Feed Page](./docs/mockup-job-feed.webp)

</details>

<details><summary>Mockup Job Page</summary>

![Job Page](./docs/mockup-job.webp)

</details>

<details><summary>Mockup Talent Feed Page</summary>

![Talent Feed Page](./docs/mockup-talent-feed.webp)

</details>

<details><summary>Mockup Talent Profile Page</summary>

![Talent Profile Page](./docs/mockup-talent-profile.webp)

</details>

<details><summary>Mockup Employer Profile Page</summary>

![Employer Profile Page](./docs/mockup-employer-profile.webp)

</details>

<details><summary>Mockup User Details Page</summary>

![User Details Page](./docs/mockup-user-details.webp)

</details>

<details><summary>Mockup Talent Profile Edit Page</summary>

![Talent Profile Edit Page](./docs/mockup-talent-profile-edit.webp)

</details>

<details><summary>Mockup Employer Profile Edit Page</summary>

![Employer Profile Edit Page](./docs/mockup-employer-profile-edit.webp)

</details>

<details><summary>Mockup Employer Job List Page</summary>

![Employer Job List Page](./docs/mockup-employer-job-list.webp)

</details>

<details><summary>Mockup Employer Job Edit Page</summary>

![Employer Job Edit Page](./docs/mockup-employer-job-edit.webp)

</details>

## Database Design

In the development of Remote Forge, I have meticulously crafted the database architecture to support a dynamic and scalable user model. To accommodate various user roles, I introduced a user_type field in the user model. This flexibility allows me to define distinct profiles and functionalities for different user types, initially implementing two primary roles: Talent and Employer.

Employers have the capability to create job listings, forming the core interaction of the platform. Each listing is directly linked to an employer, facilitating a streamlined management process. On the other side, Talents, equipped with comprehensive profile features including resumes and social links, can present a detailed professional persona.

![Database Design](./docs/db-design.webp)

During the development of Remote Forge, the database structure underwent several changes to the fields used in the models. Here is the updated version:

![Database Update](./docs/db-design-update.webp)

## Colours Scheme

For my job board website, I chose a green colour scheme. Using green can make the website more inviting and trustworthy, contributing to a positive user experience.

For the project, I use Bootstrap and override Bootstrap's primary and danger buttons with my custom green and red.

![Colour Scheme](./docs/colour-scheme.webp)

## Fonts

For "Remote Forge," I have carefully selected fonts that align with the aesthetic and functional needs of the platform. Understanding the importance of readability and design harmony, I chose two specific fonts to enhance the user interface.

- **Nunito Sans:** This font is utilized for the body text and paragraphs across the site. Nunito Sans is known for its readability and friendly appearance, making it an excellent choice for ensuring that the content is approachable and easy to digest. Its clean and balanced structure helps maintain clarity and ease of reading in longer texts, which is crucial for the detailed descriptions and information presented on the platform.

![Nunito Sans](./docs/font-nunito.webp)

- **Josefin Sans:** I selected Josefin Sans for all headings to add a touch of elegance and distinctiveness to the page layouts. Josefin Sans, with its vintage geometry and modern sensibility, provides a stylish contrast to the more rounded forms of Nunito Sans. This font is particularly effective in making headings stand out and capturing users' attention, thereby structuring content in a visually appealing and organized manner.

![Josefin Sans](./docs/font-josefin.webp)

These font choices are integral to the overall user experience, contributing not only to the visual impact of the site but also to its functionality and accessibility. By pairing Nunito Sans with Josefin Sans, I aim to create a cohesive and engaging environment that enhances both the aesthetic appeal and the usability of "Remote Forge."

## Logo

The logo for Remote Forge draws inspiration from The Armorer character in the Mandalorian movie. It reflects a blend of craftsmanship and strength, symbolizing the platform's mission to forge connections in the remote work landscape. The design incorporates elements that convey professionalism and innovation, aligning with the brand's identity.

![Logo and Favicon](./docs/logo.webp)

## Images

### Profile Images

For generating user profile images on Remote Forge, I used the Figma plugin "User Profile - Avatar." This plugin provides high-quality, diverse avatars that enhance the visual appeal and user experience of the platform. This plugin uses images from Pexels and Unsplash, which provide free images for both commercial and non-commercial use.

![Profile Images](./docs/profile-images.webp)

Plugin Licence Page

![Profile Images](./docs/profile-images-licence.webp)

## Icons

For Remote Forge, I used a combination of custom-designed icons and icons downloaded from Iconmonstr. These icons contribute to the website's visual identity and enhance the user experience.

![Icons](./docs/icons.webp)

## Pages and Features

### Front End Pages

<details><summary>Website Header Design</summary>
</details>

<details><summary>Home Page</summary>

One of the main features of the site is the search box. Used on the home page, it will redirect to the Job List page with the search criteria. Users can search jobs by keyword and also narrow the search by typing the location city. If there are no results, users are presented with the message: "No jobs found matching your criteria. Please try a different keyword or location."

![Jobs Search Home](./docs/page-home-search.webp)

Cities is another cool feature on the home page that allows users to quickly filter all jobs by a city.

![City Quick Filters](./docs/page-home-cities.webp)

Recent talent section shows the latest 6 talent items.

![Recent Talent](./docs/page-home-talent.webp)

</details>

<details><summary>About Page</summary>

A simple informational page including the recent talent section.

![Page About](./docs/page-about.webp)

</details>

<details><summary>Contact Page</summary>

The contact page includes contact details, social media links, and a contact form.

![Contact Page](./docs/page-contact.webp)

When the form is submitted, users are redirected to the success page.

![Contact Form Success](./docs/page-contact-success.webp)

An email is also sent with a confirmation and the user's email message.

![Email Confirmation](./docs/page-contact-email-confirmation.webp)

</details>

<details><summary>Jobs List Page</summary>

This page lists all jobs and allows users to use the search box to narrow the job results.

![Jobs Page](./docs/page-jobs.webp)

</details>

<details><summary>Single Job Page</summary>

This is a single job page. The top section of the page includes a header section with the job post date, location, schedule, and salary. Default text will display if these fields are not set.

The page also lists other roles posted by this company.

![Single Job Page](./docs/page-single-job.webp)

</details>

<details><summary>Talents Page</summary>

The talents page is a simple list page of all site talents.

![Talents List Page](./docs/page-talents.webp)

</details>

<details><summary>Talent Single Page</summary>

The single talent page is a Talent Profile Page. Profile pages allow logged-in employers to download the talent's CV as a PDF file.

![Single Talent Page](./docs/page-single-talent.webp)

</details>

<details><summary>Talent Sign Up Page</summary>

![Talent Sign Up Page](./docs/page-signup-talent.webp)

</details>

<details><summary>Employer Sign Up Page</summary>

![Employer Sign Up Page](./docs/page-signup-employer.webp)

</details>

<details><summary>Login Page</summary>

![Login Page](./docs/page-login.webp)

</details>

<details><summary>404 Error Page</summary>

![404 Error Page](./docs/page-error-404.webp)

</details>

<details><summary>500 Error Page</summary>

![500 Error Page](./docs/page-error-500.webp)

</details>

<details><summary>Legal Pages</summary>

![Privacy Policy](./docs/page-privacy.webp)
![Terms and Conditions](./docs/page-terms.webp)

</details>

### User and Content Management Pages

To provide a seamless experience for managing profiles and content, Remote Forge includes comprehensive backend pages for both Talents and Employers. Here’s an overview of the key functionalities:

#### Profile Management for Talent and Employers

- Update Profile: Talents and Employers can easily update their profile page with new information, ensuring their details are always current.
- Clear Profile: Talents and Employers have the option to clear their profile page. This action does not delete the profile but rather clears all fields and unpublishes the page, allowing for a fresh start without losing their account. To clear profile user need to confirm the action.

<details><summary>Profile Page</summary>

Talent:<br> ![Talent Profile](./docs/page-profile-talent.webp)

Employer:<br> ![Employer Profile](./docs/page-profile-employer.webp)

</details>

#### Account Management

On an account page both Talents and Employers can:

- Update Email or Username
- Navigate to Password Update Page

<details><summary>Account Page</summary>

Account page where users can update their email, username, and password.

![Account](./docs/page-account.webp)

</details>

### Job Management for Employers

Full CRUD Operations: Employers have full control over job listings with the ability to:

- Add Jobs: Create new job listings to attract potential Talents.
- View Jobs: Access a list of all their job listings.
- Update Jobs: Make changes to existing job listings.
- Delete Jobs: Remove job listings that are no longer relevant or needed.
- Restricted Access: Employers can only manage their own job listings. Other employers cannot update or delete jobs posted by others, ensuring data integrity and security.

<details><summary>Employer Job Add Page</summary>

Add job page.

![Add Job](./docs/page-employer-job-add.webp)

</details>

<details><summary>Employer Job Edit Page</summary>

Job edit page.

![Edit Job](./docs/page-employer-job-edit.webp)

</details>

<details><summary>Employer Job Delete Page</summary>

Delete Job modal popup.

![Delete Job](./docs/page-employer-job-delete.webp)

</details>

<details><summary>Employer Jobs List Page</summary>

A list of jobs created by the employer. On this page, employers can add, edit, or delete jobs.

![Jobs List](./docs/page-employer-jobs-list.webp)

</details>

### Django Administration

Website admins have access to manage jobs, users, and profiles for both talents and employers.

<details><summary>Jobs Section</summary>

![Jobs Section](./docs/backend-jobs.webp)

</details>

<details><summary>Employers Section</summary>

![Employers Section](./docs/backend-employers.webp)

</details>

<details><summary>Talents Section</summary>

![Talents Section](./docs/backend-talents.webp)

</details>

<details><summary>Users Section</summary>

![Users Section](./docs/backend-users.webp)

</details><br>

When a user registers, their profile is automatically created as either a Talent or Employer, depending on their role. Since admins have permissions to delete any entity in the backend, a button has been added to the user profile page to recreate a user profile if necessary.

Users themselves do not have the option to delete their profile, but they can unpublish it, which removes it from the frontend listings. Additionally, a clear button allows users to clear all fields of their profile. This action also unpublishes the profile. Users must confirm this destructive action in a popup to proceed.

## Technology used

### Languages and Libraries

- HTML
- CSS, SCSS
- Bootstrap
- JavaScript
- Python
- Django

### Version Control and Collaboration

- Git, Git Flow, GitHub, and GitKraken - used for managing source code and collaboration
- AWS Bucket - used for storing static and media files
- VSCode - for code editing and development

### Tooling

- Webpack - used for building CSS and JS bundle files
- Pytest - used for automated testing

### Design Tools

- Figma - used for wireframing and mockups
- User Profile | Avatar - used for profile images
- Adobe Illustrator - used for designing logos and icons
- DB Diagram - used for database design

### Testing and Validation

- W3C HTML Validator - For validating the HTML structure of each page.
- W3C CSS Validator - For validating the CSS.
- Web Accessibility Evaluation tool WAVE - For detecting and fixing accessibility issues.
- Google PageSpeed - For perfomance testing

### Other

- ChatGPT, Gemini - Used for content creation

## Development and Deployment

[Back to Top](#table-of-contents)

### Cloning the project

[Back to Top](#table-of-contents)

1. Install Git: If you haven't already installed Git on your computer, download and install it from the Git website. Follow the installation instructions for your operating system.
2. Create project folder `mkdir remote-forge`
3. Change to the project directory `cd remote-forge`
4. Clone the repository `git clone https://github.com/patrickhladun/remote-forge.git .`

### Environment Settings

Remote Forge uses three environments: Development, Staging, and Production.

For this project, I have split the settings into three separate files. However, this approach does not resonate with me, and for the next project, I will not use this method. After learning more, I feel there are no significant benefits to this approach at this stage, as it only creates duplication for staging and production environments. I have created a User Story to switch back to a single settings.py file and use if statements and environment variables to create environment-specific settings.

#### Development

For local development, Django uses SQLite3 for simplicity and ease of setup. The development settings are optimized for debugging and rapid iteration.

#### Staging and Production

Both staging and production environments use Heroku with the Gunicorn server, PostgreSQL as the database, and AWS for storing static and media files. For sending emails, the project uses Gmail's SMTP server. The staging setup mimics the production environment to ensure smooth transitions and accurate testing.

#### Environment Variables Template

Here is the template for environment variables that need to be set for server deployment:

```
ENVIRONMENT=
SECRET_KEY=
DATABASE_URL=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
GMAIL_EMAIL=
GMAIL_PASS=
```

### Local Development

To run the project locally for development, follow these steps:

1. [Clone the Project:](#cloning-the-project)

2. **Set Up the Database:**

   - The project is set to use SQLite3 locally. Run the following command to create the database:
     ```
     python manage.py migrate
     ```

3. **Run the Project Locally:**

   - Start the Django development server:
     ```
     python manage.py runserver
     ```

4. **Edit Styling and JavaScript:**

   - Install the required npm packages:

     ```
     npm install
     ```

   - For development, run:

     ```
     npm run dev
     ```

   - To output minimized CSS and JS bundle files for production, run:
     ```
     npm run build
     ```

### Deployment on Heroku

[Back to Top](#table-of-contents)

To deploy Remote Forge on Heroku, follow these steps:

1. Create a Heroku Account: at [sign up here](https://signup.heroku.com/).

2. Create a New App:

   - Once logged in, click on "Create New App."
   - Enter a unique app name and select the region closest to your users.

3. Select Buildpacks:

   - Add `nodejs` and `python` as the buildpacks in the "Settings" tab.

4. Configure Environment Variables:

   - In the "Settings" tab, click on "Reveal Config Vars."
   - Input all the required hidden variables - [variables template](#environment-variables-template)

5. Connect to GitHub and Deploy:
   - In the "Deploy" tab, select "GitHub" as the deployment method.
   - Connect your GitHub account and find the desired repository.
   - Enable automatic deploys and select the main branch.
   - click "Deploy Branch."

Your app should now be deployed and accessible on Heroku.

### Load Example Content

To start developing the site with example content, you can load predefined Jobs, Users, Talent, and Employer Profiles. Follow these steps to set up your database and load the example content.

#### Load Fixtures Locally

1. Ensure the database is created:<br>
   Run the following commands to create and set up the database:

```
python manage.py makemigrations
python manage.py migrate
```
2. Load example content:<br>
Run these commands in order to load the example content:

```
python manage.py loaddata user.talent.json
python manage.py loaddata user.employer.json
python manage.py loaddata job.listing.json
```

These commands will create the example content.

#### Load Example Content for Staging Site
1. Ensure the database is created:<br>
Run the following commands to create and set up the database for the staging environment:

```
DJANGO_SETTINGS_MODULE=config.settings.staging python manage.py makemigrations
DJANGO_SETTINGS_MODULE=config.settings.staging python manage.py migrate
```

2. Load example content:<br>
Run these commands in order to load the example content:

```
DJANGO_SETTINGS_MODULE=config.settings.staging python manage.py loaddata user.talent.json
DJANGO_SETTINGS_MODULE=config.settings.staging python manage.py loaddata user.employer.json
DJANGO_SETTINGS_MODULE=config.settings.staging python manage.py loaddata job.listing.json
```

Each user uses the same password for testing purposes. You can change the password if you like in the fixtures file and load the fixtures again.

## Manual testing

### Website Header and Navigation

<details><summary>As Visitor - Desktop</summary>

| Test Scenario | Steps to Reproduce | Expected Results | Actual Results |
| --- | --- | --- | --- |
| Logo Link | Click on the website logo | User is redirected to the home page | As expected |
| Home Link | Click on the Home link | User is redirected to the home page | As expected |
| About Link | Click on the About link | User is redirected to the About page | As expected |
| Jobs Link | Click on the Jobs link | User is redirected to the Jobs page | As expected |
| Talent link | Click on the Talent link | User is redirected to the Talent page | As expected |
| Employers Link | Click on the Employers link | User is redirected to the Employers page | As expected |
| Login/Sign In button | Click on the Login/Sign In button | User is redirected to the Login/Sign In page | As expected |
| Post a Job Button | Click on the Post a Job button | User is redirected to the Post a Job page | As expected |

</details>

<details><summary>As Visitor - Mobile</summary>

| Test Scenario | Steps to Reproduce | Expected Results | Actual Results |
| --- | --- | --- | --- |
| Menu toggle button | Click on the hamburger menu button | Offcanvas menu should slide in from the right to the left | As expected |
| Menu close button | Click on the Close button | Offcanvas menu should close by sliding to the right | As expected |
| Logo Link | Click on the website logo | User is redirected to the home page | As expected |
| Home Link | Click on the Home link | User is redirected to the home page | As expected |
| About Link | Click on the About link | User is redirected to the About page | As expected |
| Jobs Link | Click on the Jobs link | User is redirected to the Jobs page | As expected |
| Talent link | Click on the Talent link | User is redirected to the Talent page | As expected |
| Employers Link | Click on the Employers link | User is redirected to the Employers page | As expected |
| Login/Sign In button | Click on the Login/Sign In button | User is redirected to the Login/Sign In page | As expected |
| Post a Job Button | Click on the Post a Job button | User is redirected to the Post a Job page | As expected |

</details>

<details><summary>As Talent - Desktop</summary>

| Test Scenario | Steps to Reproduce | Expected Results | Actual Results |
| --- | --- | --- | --- |
| User avatar | User has uploaded a custom avatar | User avatar image is visible | As expected |
| User default avatar | User did not upload a custom avatar | Default user avatar is used | As expected |
| User Menu | User clicks on the avatar | Dropdown menu is opened | As expected |
| Profile link | 1. Click on avatar 2. Click on Profile link | User is redirected to user's profile page | As expected |
| Account | 1. Click on avatar 2. Click on Account link | User is redirected to the Account page | As expected |
| Log out | 1. Click on avatar 2. Click on Logout link | User is logged out and redirected to the home page | As expected |

</details>

<details><summary>As Talent - Mobile</summary>

| Test Scenario | Steps to Reproduce | Expected Results | Actual Results |
| --- | --- | --- | --- |
| User avatar | User has uploaded a custom avatar | User avatar image is visible | As expected |
| User default avatar | User did not upload a custom avatar | Default user avatar is used | As expected |
| User Menu | User clicks on the avatar | Offcanvas menu should slide in from the right to the left with user-specific links | As expected |
| Profile link | 1. Click on avatar 2. Click on Profile link | User is redirected to user's profile page | As expected |
| Account | 1. Click on avatar 2. Click on Account link | User is redirected to the Account page | As expected |
| Log out | 1. Click on avatar 2. Click on Logout link | User is logged out and redirected to the home page | As expected |

</details>

<details><summary>As Employer - Desktop</summary>

| Test Scenario | Steps to Reproduce | Expected Results | Actual Results |
| --- | --- | --- | --- |
| User avatar | User has uploaded a custom avatar | User avatar image is visible | As expected |
| User default avatar | User did not upload a custom avatar | Default user avatar is used | As expected |
| User Menu | User clicks on the avatar | Dropdown menu is opened | As expected |
| Profile link | 1. Click on avatar 2. Click on Profile link | User is redirected to user's profile page | As expected |
| Account | 1. Click on avatar 2. Click on Account link | User is redirected to the Account page | As expected |
| Jobs | 1. Click on avatar 2. Click on Jobs link | User is redirected to the Jobs page | As expected |
| Log out | 1. Click on avatar 2. Click on Logout link | User is logged out and redirected to the home page | As expected |

</details>

<details><summary>As Employer - Mobile</summary>

| Test Scenario | Steps to Reproduce | Expected Results | Actual Results |
| --- | --- | --- | --- |
| User avatar | User has uploaded a custom avatar | User avatar image is visible | As expected |
| User default avatar | User did not upload a custom avatar | Default user avatar is used | As expected |
| User Menu | User clicks on the avatar | Offcanvas menu should slide in from the right to the left with user-specific links | As expected |
| Profile link | 1. Click on avatar 2. Click on Profile link | User is redirected to user's profile page | As expected |
| Jobs | 1. Click on avatar 2. Click on Jobs link | User is redirected to the Jobs page | As expected |
| Account | 1. Click on avatar 2. Click on Account link | User is redirected to the Account page | As expected |
| Log out | 1. Click on avatar 2. Click on Logout link | User is logged out and redirected to the home page | As expected |

</details>

### Responsive Design Tests

These are manual tests for responsiveness performed in the Chrome browser using the Toggle Device Toolbar. Each device preset listed in the tool was tested to ensure the responsiveness and proper layout of the page elements.

Test Setup for Responsiveness

1. Load the home page on Chrome.
2. Launch the Toggle Device Toolbar.
3. Select each device preset listed and test the responsiveness of the elements.

<details><summary>Responsive Design Test Cases</summary>

| Test Scenario | Steps to Reproduce | Expected Results | Actual Results |
| --- | --- | --- | --- |
| Website Header | 1. Load website on Chrome. 2. Test header responsiveness for all device presets listed. | On medium and below devices, mobile navigation is used, and the mobile menu toggle is visible. For above medium, desktop menu is used, and the mobile menu toggle is hidden. | As expected |
| Home - Hero Section Responsiveness | 1. Load home page on Chrome. 2. Test responsiveness for all device presets listed. | Hero section design changes based on the device width | As expected |
| Home - How it Works Section | 1. Load home page on Chrome. 2. Test responsiveness for all device presets listed. | Icon text elements should be displayed in a column on small devices | As expected |
| Home - Featured Cities Section | 1. Load home page on Chrome. 2. Test responsiveness for all device presets listed. | Layout should adapt to the device width, on small devices links should be in a column. | As expected |
| Home - Our Best Talent | 1. Load home page on Chrome. 2. Test responsiveness for all device presets listed. | Layout should adapt to the device width, on small devices links should be in a column. | As expected |
| About - Content Section | 1. Load about page on Chrome. 2. Test content section responsiveness for all device presets listed. | Layout should adapt to the device width. Success stories should change to one column on small devices. | As expected |
| About - Our Best Talent Section | 1. Load about page on Chrome. 2. Test "Our best talent" section responsiveness for all device presets listed. | Layout should adapt to the device width, on small devices links should be in a column. | As expected |
| Jobs - Jobs List | 1. Load jobs page on Chrome. 2. Test Jobs list section responsiveness for all device presets listed. | Layout should adapt to the device width, on small devices jobs links should be in a column. | As expected |
| Single Job Page - Hero Section | 1. Load any single job page on Chrome. 2. Test hero section responsiveness for all device presets listed. | Hero section should adapt to the device width. On smaller devices hero header section and details icons items should break to one column | As expected |
| Single Job Page - Content Section | 1. Load any single job page on Chrome. 2. Test content section responsiveness for all device presets listed. | Content section should adapt to the device width. Other roles section should break to two columns. | As expected |
| Talents - Talents List | 1. Load talents page on Chrome. 2. Test responsiveness for all device presets listed. | Layout should adapt to the device width, on small devices talents card links should break to one column. | As expected |
| Single Talent Page - Hero Section | 1. Load any single talent page. 2. Test responsiveness for all device presets listed. | Page hero sections should adapt to the device width and it should break to one column on small devices. | As expected |
| Single Talent Page - Content Section | 1. Load any single talent page. 2. Test responsiveness for all device presets listed. | Page content sections should adapt to the device width and break to one column where aside (sidebar) section display below main content. | As expected |
| Employers - Employers List | 1. Load employers page on Chrome. 2. Test responsiveness for all device presets listed. | Layout should adapt to the device width, on small devices employers card links should break to one column. | As expected |
| Employer Single Page - Hero Section | 1. Load any single employer page on Chrome. 2. Test responsiveness for all device presets listed. | Hero section should adapt to the device width and break to one column on small devices. | As expected |
| Employer Single Page - Content Section | 1. Load any single employer page on Chrome. 2. Test responsiveness for all device presets listed. | Content section Open Roles should adapt to the device width and break to one column on small devices. | As expected |

</details>

### Functionality tests

<details><summary>Home Page</summary>

| Test Scenario | Steps to Reproduce | Expected Results | Actual Results |
| --- | --- | --- | --- |
| Submit empty job search form | Without filling the form fields click on search icon. | Jobs page should open and display all available jobs. | As expected |
| Search for Job by keyword only | 1. Type keyword i.e. "DevOps" in the "Find a job" field. 2. Press search icon. | Jobs page should open and display filtered by keyword results. | As expected |
| Search for Job by city only | 1. Type city in the "City" field. 2. Press search icon. | Jobs page should open and display filtered results by City. | As expected |
| Search for Job by Keyword and City | 1. Type keyword and city in the form. 2. Press search icon. | Jobs page should open and display filtered results by the Keyword and the City. | As expected |
| Featured Cities links | 1. Scroll to the Cities section. 2. Click on the link. | Jobs page should open with selected City as a filter. | As expected |
| Our best talent links | 1. Scroll to "Our best talent" section. 2. Click on the talent link. | When link is clicked selected Talent profile page should open. | As expected |
| View all talent button | 1. Scroll to "Our best talent" section. 2. Click on "View all Talent" button. | User should be redirected to talent list page. | As expected |

</details>

<details><summary>Contact Page</summary>

| Test Scenario | Steps to Reproduce | Expected Results | Actual Results |
| --- | --- | --- | --- |
| Empty Form | Submit empty form | The Form can't be submitted and Name field "Please fill out this field" validation warning is showing. | As expected |
| Only Name Field | Submit the form only with Name field | The Form can't be submitted and Email field "Please fill out this field" validation warning is showing. | As expected |
| Name and Email | Submit the form only with Name and Email fields | The Form can't be submitted and Message field "Please fill out this field" validation warning is showing. | As expected |
| Email Field | Submit the form with incorrect email | The Form can't be submitted and relevant email validation warnings are displayed. | As expected |
| All fields filled correctly | Submit correctly filled out form | The form is submitted successfully and email is sent to specified email. | As expected |

</details>

#### Admin Pages

<details><summary>Sign in Page</summary>

| Test Scenario | Steps to Reproduce | Expected Results | Actual Results |
| --- | --- | --- | --- |
| Login with wrong details | Try to log in with wrong password or not existing email. | When Sign In button is clicked error is showed "The email address and/or password you specified are not correct." | As expected |

</details>

<details><summary>User Account Page</summary>

| Test Scenario | Steps to Reproduce | Expected Results | Actual Results |
| --- | --- | --- | --- |
| Update username | 1. Change Username. 3. Save the form. | Username is updated. | As expected |
| To short username | 1. Type new Username with less than 4 characters. 3. Save the form. | The error is raised "Username must be at least 4 characters" | As expected |
| To long username | 1. Type new Username with less than 30 characters. 3. Save the form. | User is unable to type more than 30 character into the field. | As expected |
| Non alphanumeric characters | 1. Type new Username using non-alphanumeric characters. 3. Save the form. | Error is raised "Username must be alphanumeric" | As expected |
| Number first | 1. Type new Username with number first. 3. Save the form. | Error is raised "Username must start with a letter" | As expected |
| Correct email change | 1. Type new correct Email. 3. Save the form. | The form saves the new email and success notification shows up. | As expected |
| Incorrect email change | 1. Type new incorrect Email. 3. Save the form. | The error is raised "Enter a valid email address" | As expected |

</details>

<details><summary>Talent Sign up Page</summary>

| Test Scenario | Steps to Reproduce | Expected Results | Actual Results |
| --- | --- | --- | --- |
| Registration Form wrong email | 1. Fill in the form (email, username, password). 2. Submit the form. | After submitting HTML5 validation is triggered. | As expected |
| Registration Form existing username | 1. Fill in the form (email, username, password). 2. Submit the form. | After submitting the form error is showed "A user with that username already exists." | As expected |
| Registration Form existing email | 1. Fill in the form (email, username, password). 2. Submit the form. | After submitting the form error is showed "A user is already registered with this email address." | As expected |
| Registration Form | 1. Fill in the form (email, username, password). 2. Submit the form. | After successful registration user should be redirected to welcome page with Talent relevant content. | As expected |

</details>

<details><summary>Talent Profile Page</summary>

| Test Scenario | Steps to Reproduce | Expected Results | Actual Results |
| --- | --- | --- | --- |
| Saving the form | Click save button under the form. | The form saves the changes and notify the user with popup with the "Profile updated successfully." message. | As expected |
| Update profile "Is Published" status | Check or uncheck the "Is Published" checkbox. | If the "Is Published" is checked employer profile page will not be listed on the Talent page, home page and about page, when it is checked the Profile will be listed. | As expected |
| Upload Profile image | Select the image and save the form to upload the profile image. | Image is uploaded and saved. Image is displaying correctly on the employers lists. | As expected |
| Remove Profile image | Check "clear" checkbox on the profile image and save the form. | The image should be removed from the profile and default images should be used. | As expected |
| Update First Name field | Change First Name field and save the form. | When form is saved the First Name field should be successfully changed and reflected on the profile page. | As expected |
| Update Last Name field | Change Last Name field and save the form. | When form is saved the Last Name field should be successfully changed and reflected on the profile page. | As expected |
| Update Email field | Change Email field and save the form. | When form is saved the Email field should be successfully changed and reflected on the profile page. | As expected |
| Update Phone field | Change Phone field and save the form. | When form is saved the Phone field should be successfully changed and reflected on the profile page. | As expected |
| Update Company field | Change Company field and save the form. | When form is saved the Company field should be successfully changed and reflected on the profile page. | As expected |
| Update About field | Change About field and save the form. | When form is saved the About field should be successfully changed and reflected on the profile page. | As expected |
| Upload Resume | Select the resume file and save the form to upload the resume. | After saving the form resume is uploaded and Download button is showed on Profile page. | As expected |
| Upload Resume with unsupported extension | Select the resume file with different extension than (.pdf, .doc, .docx) and save the form to upload the resume. | After the form submission error is displayed "Unsupported file extension. Allowed extensions are: .pdf, .doc, .docx" | As expected |
| Update Website field | Change Website field and save the form. | When form is saved the Website field should be successfully changed and reflected on the profile page. | As expected |
| Update City field | Change City field and save the form. | When form is saved the City field should be successfully changed and reflected on the profile page. | As expected |
| Update Country field | Change Country field and save the form. | When form is saved the Country field should be successfully changed and reflected on the profile page. | As expected |
| Hide Location Icon | Remove Country and City. | Location icon should be hidden when Country and City fields are empty. | As expected |
| Add Social Media link | 1. Click on Add Item for Social Media Links. 2. Select social media page from the list. 3. Add url to your social media page. | When the form is saved the social media link is added correctly. | As expected |

</details>

<details><summary>Employer Sign up Page</summary>

| Test Scenario | Steps to Reproduce | Expected Results | Actual Results |
| --- | --- | --- | --- |
| Registration Form wrong email | 1. Fill in the form (email, username, password). 2. Submit the form. | After submitting HTML5 validation is triggered. | As expected |
| Registration Form existing username | 1. Fill in the form (email, username, password). 2. Submit the form. | After submitting the form error is showed "A user with that username already exists." | As expected |
| Registration Form existing email | 1. Fill in the form (email, username, password). 2. Submit the form. | After submitting the form error is showed "A user is already registered with this email address." | As expected |
| Registration Form | 1. Fill in the form (email, username, password). 2. Submit the form. | After successful registration user should be redirected to welcome page with Employer relevant content. | As expected |

</details>

<details><summary>Employer Profile Page</summary>

| Test Scenario | Steps to Reproduce | Expected Results | Actual Results |
| --- | --- | --- | --- |
| Saving the form | Click save button under the form. | The form saves the changes and notify the user with popup with the "Profile updated successfully." message. | As expected |
| Update profile "Is Published" status | Check or uncheck the "Is Published" checkbox. | If the "Is Published" is checked employer profile page will not be listed on the Employers page, when it is checked the Profile will be listed. | As expected |
| Update First Name field | Change First Name field and save the form. | When form is saved the First Name field should be successfully changed and reflected on the profile page. | As expected |
| Update Last Name field | Change Last Name field and save the form. | When form is saved the Last Name field should be successfully changed and reflected on the profile page. | As expected |
| Update Email field |

</details>

### Google PageSpeed Insights Tests

I tested the website's page performance using Google PageSpeed Insights. While the desktop scores are satisfactory, I am not fully happy with the mobile scores and recognize that there is room for improvement.

- Desktop Scores: The desktop performance scores are satisfactory, indicating good loading times and efficient resource usage.
- Mobile Scores: The mobile performance scores are lower than expected and need improvement to ensure a better user experience on mobile devices.

| Page | Desktop | Mobile |
| --- | --- | --- |
| [Home](https://pagespeed.web.dev/analysis/https-remote-forge-a1aedba3d120-herokuapp-com/usq5ool38z?form_factor=desktop) | 98,100,100,100 | 77,100,100,100 |
| [About](https://pagespeed.web.dev/analysis/https-remote-forge-a1aedba3d120-herokuapp-com-about/6cj9952sej?form_factor=desktop) | 99,100,100,100 | 85,100,100,100 |
| [Jobs](https://pagespeed.web.dev/analysis/https-remote-forge-a1aedba3d120-herokuapp-com-job-list/zeh06brkrv?form_factor=desktop) | 90,98,100,100 | 76,98,100,100 |
| [Single Job](https://pagespeed.web.dev/analysis/https-remote-forge-a1aedba3d120-herokuapp-com-job-8d83b12b-0e13-4a6b-92c1-26a3d7bf92f3/u9g5u82m3z?form_factor=desktop) | 97,100,100,100 | 81,100,100,100 |
| [Talents](https://pagespeed.web.dev/analysis/https-remote-forge-a1aedba3d120-herokuapp-com-talents/0sijvvjy6x?form_factor=desktop) | 98,98,100,100 | 73,98,100,100 |
| [Single Talent](https://pagespeed.web.dev/analysis/https-remote-forge-a1aedba3d120-herokuapp-com-talent-f40faef6-33f8-4a69-89d2-cf6e173e64c9/7vuxt0q04s?form_factor=desktop) | 99,95,100,100 | 81,95,100,100 |
| [Employers](https://pagespeed.web.dev/analysis/https-remote-forge-a1aedba3d120-herokuapp-com-employers/md81bmzr59?form_factor=mobile) | 98,98,100,100 | 77,98,100,100 |
| [Single Employer](https://pagespeed.web.dev/analysis/https-remote-forge-a1aedba3d120-herokuapp-com-employer-a25eac3e-4b95-41b2-af8d-10f7923f7c20/sc8fnnome1?form_factor=desktop) | 98,100,100,100 | 81,100,100,100 |
| [Contact](https://pagespeed.web.dev/analysis/https-remote-forge-a1aedba3d120-herokuapp-com-contact/tc5wi5yqrk?form_factor=desktop) | 99,100,100,100 | 87,100,100,100 |
| [Contact Success]() | 86,100,100,100 | 82,100,100,100 |
| [Privacy Policy](https://pagespeed.web.dev/analysis/https-remote-forge-a1aedba3d120-herokuapp-com-privacy-policy/6x8wd2p882?form_factor=desktop) | 98,100,100,100 | 79,100,100,100 |
| [Terms and Conditions](https://pagespeed.web.dev/analysis/https-remote-forge-a1aedba3d120-herokuapp-com-terms-conditions/1xjnwyc4zp?form_factor=desktop) | 98,100,100,100 | 79,100,100,100 |

### HTML Validation and Accessibility Testing

I conducted comprehensive HTML validation tests using the W3C validator to ensure that all pages adhere to HTML standards. Additionally, I performed accessibility checks to identify and resolve any errors and contrast issues. All pages have successfully passed these tests, ensuring they meet web standards and are accessible to users with disabilities.

Tools used:

- W3C HTML Validator: For validating the HTML structure of each page.
- Web Accessibility Evaluation tool WAVE: For detecting and fixing accessibility issues.

|Tested Page|Accesibility (WAVE)|Contrast (WAVE)|W3C HTML |Comments|
|---|---|---|---|---|
|[Home](https://remote-forge-a1aedba3d120.herokuapp.com/)|No Errors|No Contrast Errors|[No Errors](https://validator.w3.org/nu/?doc=https%3A%2F%2Fremote-forge-a1aedba3d120.herokuapp.com%2F)||
|[About](https://remote-forge-a1aedba3d120.herokuapp.com/about/)|No Errors|No Contrast Errors|[No Errors](https://validator.w3.org/nu/?doc=https%3A%2F%2Fremote-forge-a1aedba3d120.herokuapp.com%2Fabout%2F)||
|[Contact](https://remote-forge-a1aedba3d120.herokuapp.com/contact/)|No Errors|No Contrast Errors|[No Errors](https://validator.w3.org/nu/?doc=https%3A%2F%2Fremote-forge-a1aedba3d120.herokuapp.com%2Fcontact%2F)||
|[Contact Success](https://remote-forge-a1aedba3d120.herokuapp.com/contact/success/)|No Errors|No Contrast Errors|[No Errors](https://validator.w3.org/nu/?doc=https%3A%2F%2Fremote-forge-a1aedba3d120.herokuapp.com%2Fcontact%2Fsuccess%2F)||
|[Privacy Policy](https://remote-forge-a1aedba3d120.herokuapp.com/privacy-policy/)|No Errors|No Contrast Errors|[No Errors](https://validator.w3.org/nu/?doc=https%3A%2F%2Fremote-forge-a1aedba3d120.herokuapp.com%2Fprivacy-policy%2F)||
|[Terms and Conditions](https://remote-forge-a1aedba3d120.herokuapp.com/terms-conditions/)|No Errors|No Contrast Errors|[No Errors](https://validator.w3.org/nu/?doc=https%3A%2F%2Fremote-forge-a1aedba3d120.herokuapp.com%2Fterms-conditions%2F)||
|[Jobs](https://remote-forge-a1aedba3d120.herokuapp.com/job-list/)|No Errors|No Contrast Errors|[No Errors](https://validator.w3.org/nu/?doc=https%3A%2F%2Fremote-forge-a1aedba3d120.herokuapp.com%2Fjob-list%2F)||
|[Single Job](https://remote-forge-a1aedba3d120.herokuapp.com/job/8d83b12b-0e13-4a6b-92c1-26a3d7bf92f3)|No Errors|No Contrast Errors|[No Errors](https://validator.w3.org/nu/?doc=https%3A%2F%2Fremote-forge-a1aedba3d120.herokuapp.com%2Fjob%2F8d83b12b-0e13-4a6b-92c1-26a3d7bf92f3)||
|[Talents](https://remote-forge-a1aedba3d120.herokuapp.com/talents/)|No Errors|No Contrast Errors|[No Errors](https://validator.w3.org/nu/?doc=https%3A%2F%2Fremote-forge-a1aedba3d120.herokuapp.com%2Ftalents%2F)||
|[Single Talent](https://remote-forge-a1aedba3d120.herokuapp.com/talent/f40faef6-33f8-4a69-89d2-cf6e173e64c9)|No Errors|No Contrast Errors|[No Errors](https://validator.w3.org/nu/?doc=https%3A%2F%2Fremote-forge-a1aedba3d120.herokuapp.com%2Ftalent%2Ff40faef6-33f8-4a69-89d2-cf6e173e64c9)||
|[Employers](https://remote-forge-a1aedba3d120.herokuapp.com/employers/)|No Errors|No Contrast Errors|[No Errors](https://validator.w3.org/nu/?doc=https%3A%2F%2Fremote-forge-a1aedba3d120.herokuapp.com%2Femployers%2F)||
|[Single Employer](https://remote-forge-a1aedba3d120.herokuapp.com/employer/fd4351d1-3ad3-42c1-9379-1d09733e02ae)|No Errors|No Contrast Errors|[No Errors](https://validator.w3.org/nu/?doc=https%3A%2F%2Fremote-forge-a1aedba3d120.herokuapp.com%2Femployer%2Ffd4351d1-3ad3-42c1-9379-1d09733e02ae)||
|[Log In](https://remote-forge-a1aedba3d120.herokuapp.com/accounts/login/)|No Errors|No Contrast Errors|[No Errors](https://validator.w3.org/nu/?doc=https%3A%2F%2Fremote-forge-a1aedba3d120.herokuapp.com%2Faccounts%2Flogin%2F)||
|[Sign Up Talent](https://remote-forge-a1aedba3d120.herokuapp.com/accounts/signup/talent/)|No Errors|No Contrast Errors|[With Errors](https://validator.w3.org/nu/?doc=https%3A%2F%2Fremote-forge-a1aedba3d120.herokuapp.com%2Faccounts%2Fsignup%2Ftalent%2F)|I am unable to validate Sign Up Talent template as the errors comes from Allauth App Code|
|[Sign Up Employer](https://remote-forge-a1aedba3d120.herokuapp.com/accounts/signup/employer/)|No Errors|No Contrast Errors|[With Errors](https://validator.w3.org/nu/?doc=https%3A%2F%2Fremote-forge-a1aedba3d120.herokuapp.com%2Faccounts%2Fsignup%2Femployer%2F)|I am unable to validate Sign Up Employer template as the errors comes from Allauth App Code|
|[Password Reset](https://remote-forge-a1aedba3d120.herokuapp.com/accounts/password/reset/)|No Errors|No Contrast Errors|[No Errors](https://validator.w3.org/nu/?doc=https%3A%2F%2Fremote-forge-a1aedba3d120.herokuapp.com%2Faccounts%2Fpassword%2Freset%2F)||
|403 Error|No Errors|No Contrast Errors|No Errors - W3C validated by Direct Input||
|[404 Error](https://remote-forge-a1aedba3d120.herokuapp.com/not-found)|No Errors|No Contrast Errors|No Errors - W3C validated by Direct Input||
|500 Error|No Errors|No Contrast Errors|No Errors - W3C validated by Direct Input||

### Testing User Pages

|Tested Page|Accesibility (WAVE)|Contrast (WAVE)|W3C HTML |Comments|
|---|---|---|---|---|
|[Account](https://remote-forge-a1aedba3d120.herokuapp.com/account/)|No Errors|No Contrast Errors|No Errors - W3C validated by Direct Input||
|[Profile](https://remote-forge-a1aedba3d120.herokuapp.com/profile/)|With Errors|No Contrast Errors|No Errors - W3C validated by Direct Input|I can't fix the accessibility errors because they're caused by the django-jsonform app output|
|[My Jobs](https://remote-forge-a1aedba3d120.herokuapp.com/user-job-list/)|No Errors|No Contrast Errors|No Errors - W3C validated by Direct Input||
|Edit Job|With Errors|No Contrast Errors|No Errors - W3C validated by Direct Input|I can't fix the accessibility errors because they're caused by the django-jsonform app output|
|[Log out](https://remote-forge-a1aedba3d120.herokuapp.com/accounts/logout/)|No Errors|No Contrast Errors|No Errors - W3C validated by Direct Input||


### CSS Validation

[W3C CSS Validator results - No Errors Found](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fremote-forge-a1aedba3d120.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

![W3C CSS Validator results - No Errors Found](./docs/testing-css-validation.webp)

## Automated testing with Pytest

For "Remote Forge," I use pytest, a powerful testing framework for Python, to ensure the reliability and efficiency of my code. Pytest simplifies and enhances the testing process through its use of simple, scalable test cases and a suite of advanced features.

### Running Tests

To run the tests with pytest, you can use the following command in your terminal. This command will discover and run all the test cases in your project:

`pytest -rP`

For a more detailed report, run:

`pytest --cov --cov-report=html`

## Issues

- Git History - While working on project, I encountered an issue when attempting to remove a file from the Git history. I ran a command to remove the file, but it unexpectedly created duplicate commits that I couldn't clear or fix. Despite attempts to resolve the duplicates, the issue persisted.

### User Stories

- [Improve Website Performance](https://github.com/patrickhladun/remote-forge/issues/78)
- [Infinite Scroll or Pagination](https://github.com/patrickhladun/remote-forge/issues/63)
- [Application Functionality](https://github.com/patrickhladun/remote-forge/issues/57)
- [Account Deletion Feature](https://github.com/patrickhladun/remote-forge/issues/80)
- [Simplify Django Environment Settings](https://github.com/patrickhladun/remote-forge/issues/79)

### Bugs

- [Notification Close Button](https://github.com/patrickhladun/remote-forge/issues/66)
- [Social Media Fields Validation](https://github.com/patrickhladun/remote-forge/issues/67)
- [Employer Profile Email Field Validation Notice](https://github.com/patrickhladun/remote-forge/issues/69)
- [Employer Profile Phone Field Validation](https://github.com/patrickhladun/remote-forge/issues/70)
- [Job Edit Page - Details Section Validation](https://github.com/patrickhladun/remote-forge/issues/68)
- [Job Edit Page - Title Validation](https://github.com/patrickhladun/remote-forge/issues/65)
- [Fixing Form Updates on File Upload and Clear](https://github.com/patrickhladun/remote-forge/issues/81)

## Credits

- Profile Images: [User Profile | Avatar - Figma Plugin](https://janisrozenfelds.com/user-profile-plugin)
- Icons: [Iconmonstr](https://iconmonstr.com/)
- Unsplash Images:

  - [https://unsplash.com/photos/a-young...](https://unsplash.com/photos/a-young-man-wearing-a-hat-and-a-t-shirt-MZf0mI14RI0)
  - [https://unsplash.com/photos/selective...](https://unsplash.com/photos/selective-focus-photography-of-gray-cat-peeking-at-the-table-bsSIk3LV_NE)
  - [https://unsplash.com/photos/black-do...](https://unsplash.com/photos/black-dog-wearing-blue-denim-collar-K4mSJ7kc0As)
  - [https://unsplash.com/photos/closeup...](https://unsplash.com/photos/closeup-photography-of-woman-smiling-mEZ3PoFGs_k)
  - [https://unsplash.com/photos/man-tak...](https://unsplash.com/photos/man-taking-selfie-outdoors-Qk8o8S_PMTY)
  - [Unsplash - Dublin](https://unsplash.com/photos/city-skyline-during-night-time-jLi7xbYnYro)
  - [Unsplash - Warsaw](https://unsplash.com/photos/high-rise-buildings-during-night-time-xcPw1-5OHTk)
  - [Unsplash - Stockholm](https://unsplash.com/photos/white-boat-on-water-near-city-buildings-during-daytime-uF4PfwZPOR8)
  - [Unsplash - Rome](https://unsplash.com/photos/brown-dome-concrete-building-near-bridge-at-daytime-7ybKmhDTcz0)
  - [Unsplash - Berlin](https://unsplash.com/photos/city-buildings-near-body-of-water-during-daytime-1uWanmgkd5g)
  - [Unsplash - London](https://unsplash.com/photos/aerial-photography-of-london-skyline-during-daytime-Oja2ty_9ZLM)

- Articles and Videos:
  - [Python docstrings](https://www.programiz.com/python-programming/docstrings#:~:text=Standard%20conventions%20to%20write%20single%2Dline%20docstrings%3A&text=The%20closing%20quotes%20are%20on,structure%20ending%20with%20a%20period)
  - [Docstrings in Python](https://www.datacamp.com/tutorial/docstrings-python)
  - [Django user authentication with case insensitive username](https://stackoverflow.com/questions/70713647/django-user-authentication-with-case-insensitive-username)
  - [How to use multiple settings py files in django](https://medium.com/@morganhezekiah111/how-to-use-multiple-settings-py-files-in-django-97f6ead55aa7)
  - [Django project apps structure and folders](https://joeymasip.medium.com/django-project-apps-structure-and-folders-b9436cc22b98)
  - [Django Recipe Sharing Tutorial](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy)
  - [Python Django 7 Hour Course](https://www.youtube.com/watch?v=PtQiiknWUcI)

## Acknowledgments

- [**Jaimie Hemmings**](https://github.com/JaimieHemmings) - For thoroughly reviewing the project and providing valuable feedback.
- [**Greame Taylor**](https://github.com/G-Taylor) - My project mentor, for offering insightful tips on outbound calls and overall guidance.
- [**Laura Mayock**](https://www.linkedin.com/in/laura-mayock/) - For being a fantastic facilitator, running amazing weekly stand-ups, and providing excellent content and support.
