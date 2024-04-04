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
- [User Stories (all user stories are created in github issues)](#user-stories-all-user-stories-are-created-in-github-issues)
- [Agile Metodology](#agile-metodology)
- [Five Planes of UX](#five-planes-of-ux)
  - [Strategy](#strategy)
  - [Scope](#scope)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
  - [Surface](#surface)
- [Wireframes](#wireframes)
- [Mobile Wireframes](#mobile-wireframes)
- [Desktop Wireframes](#desktop-wireframes)
- [Design](#design)
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

## User Stories (all user stories are created in github issues)

## Agile Metodology

## Five Planes of UX

### Strategy

### Scope

### Structure

### Skeleton

### Surface

## Wireframes

## Mobile Wireframes

## Desktop Wireframes

## Design

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
