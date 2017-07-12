#!/usr/bin/python


import whois
import itertools


def log_if_available(is_available):
    def wrapper(*args, **kwargs):
        result = is_available(*args, **kwargs)
        if result is True:
            with open('available.out', 'w+') as f:
                f.write(args[1]['com'] + '\n')
        return result
    return wrapper


class Checkr(object):
    def __init__(self, verbs_file=None, nouns_file=None):
        self.verbs = []
        self.nouns = []
        if verbs_file:
            with open(verbs_file, 'r') as f:
                for verb in f:
                    self.verbs.append(verb.rstrip())
        if nouns_file:
            with open(nouns_file, 'r') as f:
                for noun in f:
                    self.nouns.append(noun.rstrip())

    def is_available(self, domain):
        '''
        Returns True if the domain is unregistered, False otherwise.
        '''
        result = False
        try:
            whois.query(domain)
        except Exception:
            result = True
        if result is True:
            with open('log.out', 'a') as f:
                f.write('%s\n' % domain)
        return result

    def word_to_domain(self, word, tlds=['com']):
        '''
        Converts a word to a domain such as foo.com.
        Returns a dictionary of tld: domain,
        such as {'com': 'abc.com', 'net': 'abc.net'}
        '''
        result = {}
        if not tlds:
            return result
        for tld in tlds:
            result[tld] = '%s.%s' % (word, tld)
        return result
    
    def check_web2(self, tlds=['com']):
        '''
        Returns a list of available domains.
        To every verb it appends an 'r' based on the last letter.
        '''
        results = []
        for verb in self.verbs:
            lastletter = verb[-1]
            secondtolastletter = verb[-2]
            word = verb
            if lastletter in 'aeiou' and secondtolastletter not in 'aeiou':
                word = verb[:-1]
            word = '%sr' % word
            domain = self.word_to_domain(word)
            for tld in tlds:
                if self.is_available(domain[tld]):
                    results.append(domain[tld])
                    print '-> ', domain[tld], ' <-'
                else:
                    print domain[tld], 'is not available'
        return results

    def check_as_they_are(self, tlds=['com']):
        results = []
        for word in itertools.chain(self.verbs, self.nouns):
            domain = self.word_to_domain(word)
            for tld in tlds:
                if self.is_available(domain[tld]):
                    results.append(domain[tld])
                    print '-> ', domain[tld], ' <-'
                else:
                    print domain[tld], 'is not available'
        return results

    def check_ing(self):
        results = []
        for word in itertools.chain(self.verbs, self.nouns):
            word = '%sing' % word
            domain = self.word_to_domain(word)
            for tld in tlds:
                if self.is_available(domain[tld]):
                    results.append(domain[tld])
                    print '-> ', domain[tld], ' <-'
                else:
                    print domain[tld], 'is not available'
        return results


if __name__ == '__main__':
    checkr = Checkr('verbs.in')
    for x in itertools.chain(checkr.check_web2(), checkr.check_ing()):
        print x
