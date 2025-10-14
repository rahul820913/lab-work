import random
import time

# Adjustable parameters
TOTAL_FRAMES = 10
WINDOW_SIZE = 4
LOSS_PROBABILITY = 0.2  # Probability that a frame is lost

def simulate_go_back_n(total_frames, window_size, loss_prob):
    base = 0
    next_seq_num = 0
    acked_upto = -1  # Last successfully ACKed frame

    while base < total_frames:
        # Send frames in window
        end = min(base + window_size, total_frames)
        print(f"Sending frames {base} to {end - 1}")
        time.sleep(1)

        # Simulate frame transmission
        loss_index = -1  # No loss initially

        for i in range(base, end):
            if random.random() < loss_prob:
                print(f"Frame {i} lost  — retransmitting from frame {i}...")
                loss_index = i
                break
            else:
                print(f"Frame {i} received successfully")
                acked_upto = i  # Update cumulative ACK

        if loss_index != -1:
            # Cumulative ACK up to last correctly received frame
            print(f"Cumulative ACK: {acked_upto}\n")
            print(f"Sender retransmits frames from {loss_index} to {end - 1}\n")
            time.sleep(1)
            # Go-Back-N behavior: retransmit from lost frame
            base = loss_index
            continue

        # All frames in window received successfully
        print(f"All frames {base}–{end - 1} ACKed  — cumulative ACK: {end - 1}\n")
        base = end  # Slide window forward

    print("All frames successfully transmitted ")

if __name__ == "__main__":
    simulate_go_back_n(TOTAL_FRAMES, WINDOW_SIZE, LOSS_PROBABILITY)
