# Remote Forge<!-- omit from toc -->

Welcome to Remote Forge, my creation and your gateway to the world of remote work opportunities. This platform is a result of my vision to connect talented professionals with the freedom and flexibility that remote jobs offer. Remote Forge stands as a testament to my belief that great work isn't confined to an office—it can happen anywhere.

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
- [Visuals](#visuals)
- [Logo](#logo)
- [Images](#images)
- [Icons](#icons)
- [Pages and Features](#pages-and-features)
  - [Front end pages](#front-end-pages)
    - [Website Header Design](#website-header-design)
    - [Website Footer Design](#website-footer-design)
    - [Home Page](#home-page)
    - [About Page](#about-page)
    - [Contact Page](#contact-page)
    - [Jobs List Page](#jobs-list-page)
    - [Job Single Page](#job-single-page)
    - [Talent List Page](#talent-list-page)
    - [Talent Single Page](#talent-single-page)
    - [Talent Signup Page](#talent-signup-page)
    - [Employer Signup Page](#employer-signup-page)
    - [Thank you pages](#thank-you-pages)
    - [404 Page](#404-page)
    - [Legal Pages](#legal-pages)
  - [Backend (admin) Pages](#backend-admin-pages)
    - [Talent Dashboard Page](#talent-dashboard-page)
    - [Talent Account Page](#talent-account-page)
    - [Talent Profile Edit Page](#talent-profile-edit-page)
    - [Employer Dashboard Page](#employer-dashboard-page)
    - [Employer Account Page](#employer-account-page)
    - [Employer Profile Edit Page](#employer-profile-edit-page)
    - [Employer Add Job Page](#employer-add-job-page)
    - [Employer Edit Job Page](#employer-edit-job-page)
    - [Employer Jobs List Page](#employer-jobs-list-page)
    - [Employer Applicants List Page](#employer-applicants-list-page)
- [Technology used](#technology-used)
- [Development and Deployment](#development-and-deployment)
- [Issues](#issues)
- [Unresolved Issues](#unresolved-issues)
- [Resolved Issues](#resolved-issues)
- [Testing and Validation](#testing-and-validation)
- [Functional testing](#functional-testing)
  - [Website Header on Desktop](#website-header-on-desktop)
  - [Website Header on Mobile](#website-header-on-mobile)
  - [Website Footer](#website-footer)
  - [Home Page](#home-page-1)
  - [About Page](#about-page-1)
  - [Contact Page](#contact-page-1)
  - [Thank You and 404 Error Pages](#thank-you-and-404-error-pages)
- [Google Page Insights Tests:](#google-page-insights-tests)
  - [Home Page](#home-page-2)
  - [About Page](#about-page-2)
  - [Contact Page](#contact-page-2)
  - [Thank You Contact Page](#thank-you-contact-page)
  - [Thank You Newsletter Page](#thank-you-newsletter-page)
  - [404 Error Page](#404-error-page)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
- [Further Improvements](#further-improvements)
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

To manage the project efficiently, I utilize GitHub Issues and Projects alongside a Kanban board. This setup is crucial for organizing my workflow and keeping track of progress.

My Approach Using GitHub: Epics and User Stories: I break down the development into Epics and User Stories, making the project manageable and ensuring each feature closely aligns with user needs, such as enabling talents to discover remote jobs and employers to manage job listings.

Kanban Board: My Kanban board features columns for Backlog, In Progress, Paused/on Hold, Verification/Testing and Done, offering a clear visual guide to the project's status and allowing me to efficiently manage tasks from conception to completion.

Collaboration and Transparency: Even as a solo developer, GitHub fosters a transparent approach to project management, making it easier to track progress and adjustments needed throughout the development process.

Feedback Loop: Leveraging agile principles, I incorporate user feedback directly into the development cycle, using GitHub to track and address feedback related to specific User Stories or Epics, ensuring Remote Forge evolves in response to real user needs.

By adopting agile methodology and utilizing GitHub's robust project management tools, I navigate the development of Remote Forge with agility, keeping the project aligned with its core mission of connecting the remote work community.

[Github Remote Forge Project](https://github.com/users/patrickhladun/projects/5)

### Epics

- [Epic 1: Project setup and planning](https://github.com/patrickhladun/remote-forge/issues/1)
- [Epic 2: Design and assets development](https://github.com/patrickhladun/remote-forge/issues/19)
- [Epic 3: Frontend and backend development for 'Remote Forge' MVP](https://github.com/patrickhladun/remote-forge/issues/3)
- [Epic 4: Testing deployment and documentation](https://github.com/patrickhladun/remote-forge/issues/9)

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

## Colours Scheme

## Fonts

## Visuals

## Logo

## Images

## Icons

## Pages and Features

### Front end pages

#### Website Header Design

#### Website Footer Design

#### Home Page

#### About Page

#### Contact Page

#### Jobs List Page

#### Job Single Page

#### Talent List Page

#### Talent Single Page

#### Talent Signup Page

#### Employer Signup Page

#### Thank you pages

#### 404 Page

#### Legal Pages

### Backend (admin) Pages

#### Talent Dashboard Page

#### Talent Account Page

#### Talent Profile Edit Page

#### Employer Dashboard Page

#### Employer Account Page

#### Employer Profile Edit Page

#### Employer Add Job Page

#### Employer Edit Job Page

#### Employer Jobs List Page

#### Employer Applicants List Page

## Technology used

- [DB Diagram](https://dbdiagram.io/) - used for Database Design

## Development and Deployment

## Issues

## Unresolved Issues

## Resolved Issues

## Testing and Validation

## Functional testing

### Website Header on Desktop

### Website Header on Mobile

### Website Footer

### Home Page

### About Page

### Contact Page

### Thank You and 404 Error Pages

## Google Page Insights Tests:

### Home Page

### About Page

### Contact Page

### Thank You Contact Page

### Thank You Newsletter Page

### 404 Error Page

### HTML Validation

### CSS Validation

## Further Improvements

## Credits

## Acknowledgments
