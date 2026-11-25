# Migrating from Salesforce to Twenty CRM

Moving from Salesforce to [Twenty](https://twenty.com/) works best for teams that use core CRM objects (Accounts, Contacts, Opportunities, Tasks, and Notes) and want to drop per-seat SaaS licensing. Teams that rely heavily on Apex triggers, Visualforce pages, or dozens of AppExchange packages should audit those dependencies before starting.

[Back to main catalog](../README.md) | [CRM category](../categories/crm.md)

## Expected difficulty

Medium for standard sales teams (1 to 2 weeks including data cleanup and parallel testing). High for heavily customized Salesforce Enterprise orgs with custom Apex code.

## Before you export

1. Audit active custom objects and fields in Salesforce Setup. Drop unused legacy fields instead of recreating clutter in Twenty.
2. List every active integration (email sync, web lead forms, billing webhooks, Slack alerts). Decide which ones move to Twenty's REST/GraphQL API or to an automation tool like Activepieces or Node-RED.
3. Freeze schema changes in Salesforce for the week of the cutover.

## Step 1: Export data from Salesforce

Use Salesforce Data Export (Setup -> Data -> Data Export) or Data Loader to pull UTF-8 CSV files in this order:

1. `Account.csv` (Companies)
2. `Contact.csv` (People)
3. `Opportunity.csv` (Deals)
4. `Task.csv` and `Note.csv` (Activities and notes)

Keep Salesforce record IDs in a temporary custom column (`legacy_sf_id`) so you can match parent-child relationships cleanly during import.

## Step 2: Deploy Twenty and define the schema

Deploy Twenty with Docker Compose on a VPS with at least 4 GB RAM and PostgreSQL backups enabled. Before importing CSV files:

- Recreate only the custom objects and custom fields your team actually uses.
- Configure deal pipeline stages to match your current sales stages.
- Add team members and assign workspace roles.

## Step 3: Import in dependency order

Import CSV files in strict parent-before-child order so references resolve:

1. Companies first, mapped by domain or `legacy_sf_id`.
2. People second, linked to their Company record.
3. Opportunities third, linked to Company, primary Contact, and stage.
4. Notes and open tasks last. Leave multi-year closed activity logs in an archive export unless compliance requires them in the live CRM.

For large datasets or relational imports, script the upload against Twenty's GraphQL or REST API in Python instead of relying on manual browser CSV uploads.

## Step 4: Reconnect email and run in parallel

Connect Google Workspace or Microsoft 365 mailboxes in Twenty settings so ongoing threads attach to contacts automatically. Run Salesforce in read-only mode for 14 days while sales reps work in Twenty, then verify pipeline totals and active deal counts before cancelling Salesforce seats.
