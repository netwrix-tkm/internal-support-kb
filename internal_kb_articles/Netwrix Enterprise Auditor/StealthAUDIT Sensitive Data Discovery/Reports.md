# Knowledge Base Reference Guide: Troubleshooting StealthAUDIT Sensitive Data Discovery Report Performance Issues

## Overview

This guide focuses on troubleshooting performance issues related to StealthAUDIT Sensitive Data Discovery reports in Netwrix Enterprise Auditor. These reports are critical for identifying sensitive data across an organization's infrastructure, ensuring compliance and mitigating risks. Understanding and resolving performance bottlenecks in this category is essential to maintain operational efficiency and customer satisfaction.

## Technical Background

### Key Concepts
- **StealthAUDIT Sensitive Data Discovery**: A feature within Netwrix Enterprise Auditor designed to scan and report sensitive data across file systems and databases.
- **SQL Views**: Logical representations of data derived from SQL queries. Views are often used to simplify complex queries and improve data accessibility.
- **Performance Optimization**: Techniques to improve the execution speed of SQL queries, especially when processing large datasets.

### System Context
- **SQL Server Database**: The backend database where sensitive data discovery jobs execute queries and store results.
- **Views in Use**:
  - `SA_FSDLP_MatchesView`: Contains matches for sensitive data criteria.
  - `SA_FSAA_ResourcesView`: Contains metadata about resources scanned.
- **Common Bottlenecks**: Inefficient SQL scripts, subqueries, and large data volumes can lead to prolonged execution times.

## Issue Recognition & Triage

### Symptoms
- Sensitive data discovery jobs take excessively long to complete.
- Jobs may terminate prematurely due to timeout or resource constraints.
- SQL queries return expected results but with significant delays.

### Priority Assessment
- **High Priority**: Jobs critical to compliance reporting or operational decision-making.
- **Medium Priority**: Jobs affecting routine audits but not time-sensitive.
- **Low Priority**: Non-critical jobs with minor delays.

## Diagnostic Methodology

### Systematic Approach
1. **Verify Symptoms**: Confirm job execution time and premature termination reports.
2. **Analyze SQL Query**: Review the SQL script used in the job for inefficiencies.
3. **Assess Data Volume**: Count rows returned by the query to understand the scale of data being processed.
4. **Test Query Performance**: Run the SQL script directly in SQL Server Management Studio (SSMS) to measure execution time.
5. **Optimize Query**: Rewrite the SQL script to eliminate inefficiencies, such as subqueries.
6. **Validate Results**: Ensure the optimized query returns the same data with improved performance.

## Information Collection

### Customer Queries
- What is the average execution time of the job?
- Has the job ever completed successfully? If so, what was the previous execution time?
- Are there any recent changes to the environment (e.g., increased data volume, SQL Server updates)?

### Logs and Data to Collect
- Original SQL script used in the job.
- Execution plan of the SQL query (from SSMS).
- Row counts from the views involved (`SA_FSDLP_MatchesView` and `SA_FSAA_ResourcesView`).
- System resource utilization during job execution (CPU, memory, disk I/O).

## Common Scenarios & Solutions

### Scenario 1: Inefficient SQL Script
**Symptoms**: Job execution time increases as data volume grows.  
**Resolution**: Optimize the SQL script by removing subqueries and simplifying joins.  

### Scenario 2: Large Data Volume
**Symptoms**: Job processes millions of rows, leading to prolonged execution times.  
**Resolution**: Implement indexing on key columns in the database to improve query performance.

### Scenario 3: Resource Constraints
**Symptoms**: Job terminates prematurely due to insufficient system resources.  
**Resolution**: Allocate additional resources (CPU, memory) to the SQL Server instance or schedule jobs during off-peak hours.

## Detailed Case Studies

### Case Study: Ticket ID [500Qk00000Bv17VIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Bv17VIAR/view)

#### Initial Symptoms
The customer reported that an "Active Sensitive Data" job was taking approximately 47 minutes to run and was terminating prematurely.

#### Diagnostic Steps
1. **Data Volume Assessment**: The support engineer requested row counts from the views involved (`SA_FSDLP_MatchesView` and `SA_FSAA_ResourcesView`).
2. **SQL Query Analysis**: The original SQL script was reviewed and identified as inefficient due to the use of subqueries.
3. **Performance Testing**: The original query was executed in SSMS, confirming prolonged execution time.

#### Key Information Leading to Solution
- The original SQL script relied on subqueries, which increased execution time as data volume grew.
- Row counts indicated the job was processing 642,016 rows.

#### Resolution
The support engineer provided an optimized SQL script:
```sql
IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].SA_Active_Sensitive_Data_Result') AND type in (N'V'))
DROP VIEW SA_Active_Sensitive_Data_Result

GO

CREATE VIEW [SA_Active_Sensitive_Data_Result] AS
SELECT mv.[HostName], mv.[CriteriaName], mv.[FileName], mv.[FilePath], mv.[MatchCount]
FROM dbo.SA_FSDLP_MatchesView mv
JOIN dbo.SA_FSAA_ResourcesView rv ON mv.ResourceID = rv.ID
WHERE rv.DeletedUSN IS NULL
```
After implementing the optimized script, the job execution time was reduced to 29 seconds while returning the same number of rows.

#### Key Takeaways
- Subqueries should be avoided in SQL scripts for large datasets.
- Performance testing in SSMS is essential to validate optimizations.
- Monitoring data growth is critical to proactively address performance issues.

#### Efficiency Improvements
- Regularly review SQL scripts for optimization opportunities.
- Implement indexing on frequently queried columns.

## Best Practices & Tips

1. **SQL Optimization**: Avoid subqueries and use direct joins wherever possible.
2. **Performance Testing**: Always test SQL scripts in SSMS before deploying changes.
3. **Resource Monitoring**: Monitor system resource utilization during job execution to identify bottlenecks.
4. **Proactive Maintenance**: Periodically review and optimize SQL scripts as data volume grows.
5. **Customer Communication**: Clearly explain the changes made and their impact on performance.

## Escalation Guidelines

### Criteria for Escalation
- Performance issues persist despite SQL optimization.
- Jobs critical to compliance or business operations fail repeatedly.
- Resource constraints cannot be resolved within the customer's environment.

### Escalation Procedure
1. Document all troubleshooting steps and results.
2. Provide detailed logs, execution plans, and row counts.
3. Escalate to the development team for advanced SQL optimization or product updates.
4. Communicate escalation status and expected timelines to the customer.