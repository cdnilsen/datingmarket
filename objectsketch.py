import datetime

contractID = 1001
class endUser:
    def __init__(self, endUserID, userName, passwordHash, creditHash, inviterID, currentMatchmakerID, currentContractID):
        self.endUserID = endUserID
        self.userName = userName
        self.passwordHash = passwordHash
        self.creditHash = creditHash
        self.inviterID = inviterID
        self.currentMatchmakerID = currentMatchmakerID
        self.currentContractID = currentContractID

    def weighBid(offeringMatchmaker, monthlyBid, matchmakerCost, closingBid):
        bidAccepted = input("Accept a bid for $" + str(monthlyBid) + " monthly and a closing fee of $" + str(closingBid) + "? (y/n)")
        if bidAccepted == "y":
            newContract = Contract(contractID, datetime.now(), self.endUserID, offeringMatchmaker[matchmakerID], inviterID, monthlyBid, matchmakerCost, closingBid)
            self.currentContractID = newContract[contractID]
            self.currentMatchmakerID = offeringMatchmaker[matchmakerID]
            offeringMatchmaker.currentContracts.append(newContract)
            contractID += 1
        



class Contract:
    def __init__(self, contractID, dateEstablished, endUserID, matchmakerID, inviterID, monthlyCost, matchmakerCost, closingCost):
        self.contractID = contractID
        self.dateEstablished = dateEstablished
        self.endUserID = endUserID
        self.subscriberID = subscriberID
        self.matchmakerID = matchmakerID
        self.inviterID = inviterID
        self.monthlyCost = monthlyCost
        self.matchmakerCost = matchmakerCost
        self.closingCost = closingCost
    

class Matchmaker:
    def __init__(self, matchmakerID, matchmakerName, passwordHash, creditHash, currentContracts):
        self.matchmakerID = matchmakerID
        self.matchmakerName = matchmakerName
        self.passwordHash = passwordHash
        self.creditHash = creditHash
        self.inviterID = inviterID
        self.currentContractID = currentContracts

    def offerBid(self, endUser, contractID, monthlyBid, matchmakerCost, closingBid):
        endUser.weighBid(self.matchmakerID, monthlyBid, matchmakerCost, closingBid)

