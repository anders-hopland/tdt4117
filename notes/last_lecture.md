# Last lecture before exam

## Data retrieval vs information retrieval:
* 	| Data retreival | Information retrieval
* Content | Data 	 | Information
Skriv mer her

## Introduction
* Ir systems usually adopt index terms to process queries
* Index terms
	* A keyword or a group of selecterc words
	* One word or more in general
Manlger litt her

## The boolean model
* Simple model based on set theroy
* Queries specified as boolean expressions (Like in Intro AI TDT4136 set theroy)
	* Precise semantics
	* Neat formalism
* Terms either present or absent, no partial match, which means no ranking
* Drawbacks of the boolean model
	* No partial matching
	* No ranking
	* Must translate information into a boolean expression, which is difficult for much users
	* Queries made by users are often too simplistic
	* Does most often return too few or too many documents

## Vector space model
* A document can be returned on parital match
* Paste the picture from the lecture foils
* Similarity based on cosine between the query vector and the document vector
* Weights based on term frequency and inverse document frequency
* Best term weighing factor: w_i, j = f_i * idf_i,j

## Probbilistic ranking priciple
* Given a user query q and a document dj
	* Trying to estimate the probability the user would find dj interesting/relevant
	* This is the odds of dj being relevant
	* Taking the odds minimizer the proability of an errounous judgement

* Definition
	* w_i,j = Element {0, 1}
	* P(R | d_j): Probability that given document is relevant

* Matching: P(R | Q, d), formula for relevance
* Pros of probabilistic model:
	* Docs ranked in decreasing order
* cons
	* Need to guess estimate for P(k_i | R)
	* One more

## Brief comparison of classic models
* See lecture foils

## IR based on language model (LM)
* A common search heuristic is to use words you expect to find in matching documents as your query
* The LM approach exploits this idea


## Precision and recall
* Precision: True positives / (true positives + false positives)
* Recall: True positives / All relevant
* Trade off between precision and recall
* Recall / Precision: See foils, same as one of the excersices

## MAP (Mean average precision)
* Average of the precision 

## Interpolated precision
* Precision not measured at exact recall level
	* Use precision at next highest level of recall
* Makes it esasier to compare IR systems
* The graph should always end at 0

## R precision
* Precision at the Rth position in the ranking of results for a query that has R relevant documents
* See foils (!Important, could come on exam)

## E measure (Parametirized F Measure)
* A variant if F measure that allows weighingemphasis on precision or recall
* See foils for formula 
* Must know what E and F measure are, really important to know including equeations for exam

## Relevance feedback architecture
* Enhance the query by letting the user reformulate the query (see drawing on foils)
* Rochio update method (See formula on foils)
	* Only used in the vector space model
* Ide regular:
	* Same as rochio but no normalization
* Ide "Dec Hi" Method
	* Rejecting just the highest ranked of the non relevant documents

## Use document collection to construct thesaurus
* Analyze the text in the docuemnt store
* Global:
	* Build a thesaurus from all docuemnts
* Local:
	* First retrieve docuemnts based on initial query
	* Build a thesaurus from those documents
* Expand query using thesaurus
	* Reurn query
* Pseudo relevance feedback
	* Simulating the user relevance feedback, saying that e.g the 10 first are relevant and then use the methods above
	* Performs better than user relevance feedback with a large document collection
* One of the main drawbacks of thesaurus is that you can get results with words that are not connected, which betters recall but worsens precision
* Docuemt preprocessing:
	* Lexical analysis
	* Stopwords elimination
	* Stemming
	* Index term selection
	* Thesauri
* Text compression
	* Statistical methods
	* Dcitionary methods
	* Inverted file compression

## Pagerank
* Developed and part of google
* q: Probability that a user randomly jumps to the page
* 1 - q: Probability that a user visits the page followeing a link
* L(a): number of outgoing links of page a
* p_1, ..., p_n: pages pointing to page a
* Algorithm: see foils
