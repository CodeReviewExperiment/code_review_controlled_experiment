library(exact2x2)
library(xtable)
library(effsize)
library(nortest)

setwd("") # folder path

languages=c("Java","Python")
treatments=c("NCR","ACR","CCR")
test_sep <- " \\emph{vs} "

#LOAD DATA
data<-read.csv("raw-data.csv")

#SPLIT BY TREATMENT
data_NCR<-data[which(data["treatment"] == 'no code review'),]
data_ACR<-data[which(data["treatment"] == 'automated code review'),]
data_CCR<-data[which(data["treatment"] == 'comprehensive code review'),]

#SPLIT BY LANGUAGE
data_python<-data[which(data["programming.language"] == 'Python'),]
data_java<-data[which(data["programming.language"] == 'Java'),]

data_python_NCR<-data_python[which(data_python["treatment"] == 'no code review'),]
data_python_ACR<-data_python[which(data_python["treatment"] == 'automated code review'),]
data_python_CCR<-data_python[which(data_python["treatment"] == 'comprehensive code review'),]

data_java_NCR<-data_java[which(data_java["treatment"] == 'no code review'),]
data_java_ACR<-data_java[which(data_java["treatment"] == 'automated code review'),]
data_java_CCR<-data_java[which(data_java["treatment"] == 'comprehensive code review'),]


run_stat_analysis <- function(dependent_variable){
  combinations = list(t1 = c(), t2 = c(), label = c())
  
  # Create a list of all allowed combinations for statistical tests
  for (treatment1 in treatments) {
    for (treatment2 in treatments) {
      if (treatment1 != treatment2) {
        if (!(paste(treatment1, treatment2, sep=test_sep) %in% combinations$label) & !(paste(treatment2, treatment1, sep=test_sep) %in% combinations$label)) {
          combinations$t1 = c(combinations$t1, treatment1)
          combinations$t2 = c(combinations$t2, treatment2)
          combinations$label = c(combinations$label, paste(treatment1, treatment2, sep=test_sep))
        }
      }
    }
  }
  
  pdf(paste(dependent_variable,".pdf"))
  boxplot(na.omit(eval(parse(text = paste("data_NCR$",dependent_variable,sep="")))), na.omit(eval(parse(text = paste("data_ACR$",dependent_variable,sep="")))), na.omit(eval(parse(text = paste("data_CCR$",dependent_variable,sep="")))),
          na.omit(eval(parse(text = paste("data_python_NCR$",dependent_variable,sep="")))), na.omit(eval(parse(text = paste("data_python_ACR$",dependent_variable,sep="")))), na.omit(eval(parse(text = paste("data_python_CCR$",dependent_variable,sep="")))),
          na.omit(eval(parse(text = paste("data_java_NCR$",dependent_variable,sep="")))), na.omit(eval(parse(text = paste("data_java_ACR$",dependent_variable,sep="")))), na.omit(eval(parse(text = paste("data_java_CCR$",dependent_variable,sep="")))),
          col="gray", boxwex = 0.5, axes=TRUE, 
          names=c("Overall\nNCR","Overall\nACR","Overall\nCCR", "Python\nNCR","Python\nACR","Python\nCCR", "Java\nNCR","Java\nACR","Java\nCCR"))
  dev.off()
  
  res = list(Test = c(), p = c(), d = c())
  
  for (i in 1:length(combinations$t1)) {
    label <- combinations$label[i]
    treatment1 <- combinations$t1[i]
    treatment2 <- combinations$t2[i]
    
    distribution1 <- na.omit(eval(parse(text = paste("data_",treatment1,"$",dependent_variable,sep=""))))
    distribution2 <- na.omit(eval(parse(text = paste("data_",treatment2,"$",dependent_variable,sep=""))))
    
    suppressWarnings({
    
    p.value=wilcox.test(distribution1,
                        distribution2,
                        paired=FALSE)$p.value
    })
    cliff=cliff.delta(distribution1,
                      distribution2,
                      paired=FALSE)$estimate
    
    res$Test = c(res$Test, label)
    res$p = c(res$p, p.value)
    res$d = c(res$d, cliff) 
  }
  
  res$p = p.adjust(res$p, method = "BH")
  
  print(paste("### ",dependent_variable,sep=""))
  for (i in 1:length(res$p)) {
    print(paste(res$Test[i],res$p[i],res$d[i],sep=" & "))
  }
  
}


#####################################################
# RQ0: Is there a statistically significant difference 
# in the characteristics of the code reviews written 
# with and with- out automated support?
#####################################################

run_stat_analysis("total.issues.reported")
run_stat_analysis("number.of.sentences")
run_stat_analysis("number.of.words")
run_stat_analysis("total.coverage")
run_stat_analysis("code.coverage")
run_stat_analysis("doc.coverage")


#####################################################
# RQ1: To what extent does automated code review 
# increase the likelihood of identifying code quality 
# issues?
#####################################################

run_stat_analysis("injected.issues.identified")
run_stat_analysis("X..injected.issues.identified")


#####################################################
# RQ2: To what extent does the availability of an 
# automated code review save time during the code 
# inspection?
#####################################################

run_stat_analysis("total.time..s")
run_stat_analysis("time.on.code.to.review")
run_stat_analysis("time.writing.code.review")



#####################################################
# RQ3: Does the availability of an automated code 
# review increase the reviewers' confidence?
#####################################################

run_stat_analysis("confidence")