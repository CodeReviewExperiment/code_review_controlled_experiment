library(exact2x2)
library(effsize)
library(dunn.test)
library(lmPerm)
setwd("") # folder path


#####################################################
# RQ0: Is there a statistically significant difference 
# in the characteristics of the code reviews written 
# with and with- out automated support?
#####################################################

data<-read.csv("RQ0-2-3-raw-data.csv")
attach(data)

# NUMBER OF SENTENCES
# Linear model
model <- lm(number.of.sentences ~ relevel(factor(treatment), ref = "MCR") + years.of.experience + role.in.code.review + programming.language + project)
summary(model)

# Analysis of treatment with Dunn test
dunn.test(number.of.sentences,treatment,method="bh")
# Analysis of cofactors with permutation test
summary(aovp(number.of.sentences~treatment + years.of.experience + role.in.code.review + programming.language + project,perm="Prob",maxIter=500000,nCycle=100,Ca=0.001))


# NUMBER OF COMMENTED LINES
# Linear model
model <- lm(number.of.commented.lines ~ relevel(factor(treatment), ref = "MCR") + years.of.experience + role.in.code.review + programming.language + project)
summary(model)

# Analysis of treatment with Dunn test
dunn.test(number.of.commented.lines,treatment,method="bh")
# Analysis of cofactors with permutation test
summary(aovp(number.of.commented.lines~treatment + years.of.experience + role.in.code.review + programming.language + project,perm="Prob",maxIter=500000,nCycle=100,Ca=0.001))


# NUMBER OF REPORTED ISSUES
# Linear model
model <- lm(total.issues.reported ~ relevel(factor(treatment), ref = "MCR") + years.of.experience + role.in.code.review + programming.language + project)
summary(model)

# Analysis of treatment with Dunn test
dunn.test(total.issues.reported,treatment,method="bh")
# Analysis of cofactors with permutation test
summary(aovp(total.issues.reported~treatment + years.of.experience + role.in.code.review + programming.language + project,perm="Prob",maxIter=500000,nCycle=100,Ca=0.001))



#####################################################
# RQ1: To what extent does automated code review 
# increase the likelihood of identifying code quality 
# issues?
#####################################################

logit_data<-read.csv("RQ1-issues-logit-data.csv")

attach(logit_data)
model <- glm(formula = Is.injected.issue.identified ~ relevel(factor(treatment), ref = "MCR") + years.of.experience + role.in.code.review + programming.language + project + issue.type, family = "binomial")

results <- summary(model)
results
OR <- exp(results$coefficients[,1])
OR


# Including issue severity
model <- glm(formula = Is.injected.issue.identified ~ relevel(factor(treatment), ref = "MCR") + years.of.experience + role.in.code.review + programming.language + project + issue.type + issue.severity, family = "binomial")

#####################################################
# RQ2: To what extent does the availability of an 
# automated code review save time during the code 
# inspection?
#####################################################
# TOTAL TIME
# Linear model
model <- lm(total.time ~ relevel(factor(treatment), ref = "MCR") + years.of.experience + role.in.code.review + programming.language + project)
summary(model)

# Analysis of treatment with Dunn test
dunn.test(total.time,treatment,method="bh")
# Analysis of cofactors with permutation test
summary(aovp(total.time~treatment + years.of.experience + role.in.code.review + programming.language + project,perm="Prob",maxIter=500000,nCycle=100,Ca=0.001))


# TIME REVIEW
# Linear model
model <- lm(time.on.code.to.review ~ relevel(factor(treatment), ref = "MCR") + years.of.experience + role.in.code.review + programming.language + project)
summary(model)

# Analysis of treatment with Dunn test
dunn.test(time.on.code.to.review,treatment,method="bh")
# Analysis of cofactors with permutation test
summary(aovp(time.on.code.to.review~treatment + years.of.experience + role.in.code.review + programming.language + project,perm="Prob",maxIter=500000,nCycle=100,Ca=0.001))


# TIME WRITING
# Linear model
model <- lm(time.writing.code.review ~ relevel(factor(treatment), ref = "MCR") + years.of.experience + role.in.code.review + programming.language + project)
summary(model)

# Analysis of treatment with Dunn test
dunn.test(time.writing.code.review,treatment,method="bh")
# Analysis of cofactors with permutation test
summary(aovp(time.writing.code.review~treatment + years.of.experience + role.in.code.review + programming.language + project,perm="Prob",maxIter=500000,nCycle=100,Ca=0.001))


#####################################################
# RQ3: Does the availability of an automated code 
# review increase the reviewers' confidence?
#####################################################

# CONFIDENCE
# Linear model
model <- lm(confidence ~ relevel(factor(treatment), ref = "MCR") + years.of.experience + role.in.code.review + programming.language + project)
summary(model)

# Analysis of treatment with Dunn test
dunn.test(confidence,treatment,method="bh")
# Analysis of cofactors with permutation test
summary(aovp(confidence~treatment + years.of.experience + role.in.code.review + programming.language + project,perm="Prob",maxIter=500000,nCycle=100,Ca=0.001))
