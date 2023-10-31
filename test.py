from SSD_Model import ssdModel


block_error_rate = [0.0001, 0.00015, 0.0003, 0.0006]
cnt = [990, 2, 2, 2, 2]
PE = [1000, 5000, 7000, 10000]

t = ssdModel(block_error_rate, cnt, PE)
print('ssd\t\t  ',t.get_SSD_error_rate())
print('channel\t' ,t.channel_error_rate)
print('chip\t  ', t.chip_error_rate)
print('die\t\t  ', t.die_error_rate)
print('block\t  ', t.block_error_rate)
